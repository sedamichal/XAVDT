from great_tables import GT


class GTStyle:
    def __init__(self):
        import os

        super().__setattr__("_api_key", os.getenv("MY_APP_API_KEY", "12345"))
        super().__setattr__("_style", {})
        self._set_defaults()

    def apply(self, GT: GT) -> GT:
        return GT.tab_options(**self._style)

    def _set_defaults(self):
        defaults = {
            "heading_background_color": "#b8b8b8",
            "column_labels_font_weight": "bold",
            "table_body_hlines_style": "solid",  # Horizontální linky
            "table_body_vlines_style": "solid",  # Vertikální linky
            "table_body_hlines_color": "#d3d3d3",  # Světle šedá barva linek
            "table_body_vlines_color": "#d3d3d3",
            "table_body_hlines_width": "1px",
            "table_body_vlines_width": "1px",
            "column_labels_vlines_style": "solid",
            "column_labels_vlines_color": "#d3d3d3",
            "column_labels_border_top_style": "solid",
            "column_labels_border_top_color": "#d3d3d3",
            "column_labels_border_bottom_style": "solid",
            "column_labels_border_bottom_color": "#d3d3d3",
        }
        self._style.update(defaults)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            self._style[name] = value

    @property
    def style(self):
        return self._style
