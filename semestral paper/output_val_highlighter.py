import numpy as np
import pandas as pd
import re
from great_tables import GT, style, loc
from dataclasses import dataclass

from abc import ABC, abstractmethod


@dataclass
class OutputStyle:
    bg_color: str | None = None
    fg_color: str | None = None
    text_wieght: str | None = None


class OutputStyleDict(dict):
    def __setitem__(self, key: int, value: OutputStyle):
        return super().__setitem__(key, value)

    def __getitem__(self, key: int):
        if key in self:
            return super().__getitem__(key)
        else:
            return OutputStyle()


class MaxMinValRowHighliter(ABC):
    def __init__(
        self,
        value_column: str,
        style: OutputStyle
    ):
        self._value_column = value_column
        self._style = style

    def apply(self, df: pd.DataFrame = None, gt: GT = None):
        gt_obj = GT(df) if gt == None else gt

        text_style = style.text(color=self._style.fg_color, weight=self._style.text_wieght)

        rows = self._get_rows(df)

        gt_obj = gt_obj.tab_style(style=text_style, locations=loc.body(rows=rows))

        return gt_obj

    @abstractmethod
    def _get_rows(self, df: pd.DataFrame):
        pass

class MaxValueRowHighliter(MaxMinValRowHighliter):

    def _get_rows(self, df: pd.DataFrame):
        return [df[self._value_column].idxmax()]

class MinValueRowHighliter(MaxMinValRowHighliter):

    def _get_rows(self, df: pd.DataFrame):
        return [df[self._value_column].idxmin()]


class ValHighliter:
    def __init__(
        self,
        columns_mask,
        th_column_mask,
        treshold,
        styles: OutputStyleDict,
        lower=True,
    ):
        self._th = treshold
        self._lower = lower
        self._columns_mask = columns_mask
        self._th_columns_mask = th_column_mask
        self._treshold = treshold
        if not isinstance(styles, OutputStyleDict):
            self._styles = OutputStyleDict(styles)
        else:
            self._styles = styles

    def _get_index_range(self, df) -> int | None:
        if self._columns_mask == "*":
            return range(1)

        cols = df.columns
        indices = []

        pattern = fr"^{self._columns_mask.replace('*', r'(\d+)')}"

        for col in cols:
            match = re.search(pattern, col)
            if match:
                val = int(match.group(1))
                if val not in indices:
                    indices.append(int(match.group(1)))

        return indices

    def _get_index_columns(self, df, index):
        if self._columns_mask == "*":
            return df.columns.tolist()

        cols = df.columns
        columns = []

        pattern = rf"^{self._columns_mask.replace('*', str(index))}(?:\D+.*)?"

        for col in cols:
            match = re.fullmatch(pattern, col)
            if match:
                columns.append(col)
        return columns

    def _get_index_th_column(self, df, index):
        if self._columns_mask == "*":
            return self._th_columns_mask

        cols = df.columns

        pattern = rf"^{self._th_columns_mask.replace('*', str(index))}"

        for col in cols:
            match = re.search(pattern, col)
            if match:
                return col

    def apply(self, df: pd.DataFrame, gt: GT = None):
        gt_obj = GT(df) if gt == None else gt

        for i in self._get_index_range(df):
            th_column = self._get_index_th_column(df, i)
            columns = self._get_index_columns(df, i)
            if self._lower:
                rows = lambda x: x[th_column] <= self._treshold
            else:
                rows = lambda x: x[th_column] >= self._treshold

            _style = self._styles[i]
            text_style = style.text(color=_style.fg_color, weight=_style.text_wieght)
            gt_obj = gt_obj.tab_style(
                style=text_style, locations=loc.body(columns=columns, rows=rows)
            )
            row_style = style.fill(_style.bg_color)
            gt_obj = gt_obj.tab_style(
                style=row_style, locations=loc.body(columns=columns, rows=rows)
            )

        return gt_obj
    
    def apply_max(self, df: pd.DataFrame, gt: GT = None):
        pass
