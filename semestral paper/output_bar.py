import pandas as pd
from abc import ABC, abstractmethod


class Bar(ABC):

    def output(
        self,
        df,
        column,
        bar_column_name=None,
        bar_column_suffix=None,
        bar_column_prefix=None,
    ):

        bar_col_name = self._get_bar_column_name(
            bar_column_name, bar_column_suffix, bar_column_prefix
        )

        df = self._add_bar_column(df, column, bar_col_name)

        if bar_col_name != bar_column_name:
            df.format({bar_col_name: ""})

        self._output(df, column, bar_col_name)

        return df

    @abstractmethod
    def _output(self, df, column, bar_col_name):
        pass

    def _add_bar_column(self, df, column, bar_column_name):
        idx = df.columns.get_loc(column)

        if bar_column_name not in df.columns:
            df.insert(loc=idx + 1, column=bar_column_name, value="")

        return df

    def _get_bar_column_name(
        self, column, bar_column_name=None, bar_column_suff=None, bar_column_prefix=None
    ):
        if bar_column_name != None:
            return bar_column_name

        parts = []

        if bar_column_prefix != None:
            parts.append(bar_column_prefix)

        parts.append(column)

        if bar_column_suff != None:
            parts.append(bar_column_suff)

        return "_".join([p for p in parts if p])

    def _get_max_value(self, df, column):
        total_sum = df[column].sum()

        if total_sum in [1, 100]:
            max_value = total_sum
        else:
            max_value = df[column].max()

        return max_value

    def _get_style_matrix(self, df):
        style_df = pd.DataFrame("", index=df.index, columns=df.columns)

        for i in self._get_index_range(df):
            th_column = self._get_index_th_column(df, i)

            for col in self._get_index_columns(df, i):
                mask = df[th_column] <= self._th
                style_df.loc[mask, col] = self._style[i]

        return style_df


class CssBar(Bar):
    def _output(self, df, column, bar_col_name):
        if hasattr(df, 'bar'):
            df = df.bar(
                subset=[bar_col_name], vmin=0, vmax=self._get_max_value(df.data, column)
            )            
        else:
            df = df.style.bar(
                subset=[bar_col_name], vmin=0, vmax=self._get_max_value(df, column)
            )
        return df


class AnsiBar(Bar):

    def __init__(self, width=10, filled_char="█", not_filled_char="░"):
        super().__init__()
        self._width = width
        self._not_filled_char = not_filled_char
        self._filled_char = filled_char

    def _output(self, df, column, bar_col_name):
        df[bar_col_name] = df[column].apply(
            lambda x: self._render_cli_bar(
                x, self._get_max_value(df, column), self._width, self._not_filled_char
            )
        )
        return df

    def _render_cli_bar(self, val, max_val, width, not_filled_char):
        percent = (float(val) / float(max_val)) * 100 if max_val != 0 else 0

        clamped_percent = max(0, min(100, percent))
        filled = int(round(width * clamped_percent / 100))

        bar = self._filled_char * filled + not_filled_char * (width - filled)

        if self._filled_char == "|":
            output = f"{bar}"
        else:
            output = f"|{bar}|"            

        return output


__all__ = ["CssBar", "AnsiBar"]
