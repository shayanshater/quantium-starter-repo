from main_2 import update_graph


def test_header_exists(dash_duo):
    dash_duo.start_server(update_graph)
    dash_duo.wait_for_element("#Header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(update_graph)
    dash_duo.wait_for_element("#graph", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(update_graph)
    dash_duo.wait_for_element("#radio", timeout=10)


    

