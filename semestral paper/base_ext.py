import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

from great_tables import GT, style, loc
from GT_style import GTStyle
from IPython.display import HTML, display


class ExtBase:

    def __init__(
        self, data: pd.DataFrame, target_column, excluded_columns=[]
    ):
        self._excluded_columns = excluded_columns
        self._target_column = target_column
        self._data = data
        self._X = self._get_X()
        self._y = self._data[self._target_column]
        self._feature_names = self._get_feature_names()

    def _get_feature_names(self):
        return self._data.columns.drop(self._excluded_columns)
    
    def _get_target_values(self):
        target_values = self._data[self._target_column].unique()
        target_values.sort()
        return target_values
    
    def _get_target_values_count(self):
        target_values = self._get_target_values()
        return len(target_values)

    def _get_X(self):
        X = self._data.drop(columns=self._excluded_columns)
        scaler = StandardScaler()
        return scaler.fit_transform(X)

    def _pipe_table_style(self, gt: GT) -> GT:
        return gt.tab_options(**GTStyle().style)

    def _get_colors_map(self):
        target_values = self._get_target_values()
        n_colors = len(target_values)
        colors = plt.cm.rainbow(np.linspace(0, 1, n_colors))

        return zip(colors, target_values)
        

    def _display_gt_html(self, gts: list[GT]):
        html_code = f"""
        <div style="display: flex; flex-direction: column; gap: 20px;">
        """

        for gt in gts:
            html_code += f"""
                {gt._repr_html_()}
            """

        html_code += f"""
        </div>
        """

        display(HTML(html_code))
