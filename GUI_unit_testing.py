# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import pytest
from PyQt5 import QtCore

import GUI


@pytest.fixture
def app(qtbot):
    test_ui_app = GUI.WebServerUI()
    qtbot.addWidget(test_ui_app)

    return test_ui_app


def test_port_label(app):
    assert app.text_label.text() == "Port Select:"


def test_port_input_server_off(app, qtbot):
    qtbot.keyClick(app.portInput, 'a', QtCore.Qt.ControlModifier)  # CTRL + A
    qtbot.keyClicks(app.portInput, '5741')
    assert app.portInput.text() == "5741"


def test_port_input_server_on(app, qtbot):
    qtbot.keyClick(app.portInput, 'a', QtCore.Qt.ControlModifier)  # CTRL + A
    qtbot.keyClicks(app.portInput, '5741')
    app.startButton.click()
    qtbot.keyClick(app.portInput, 'a', QtCore.Qt.ControlModifier)  # CTRL + A
    qtbot.keyClicks(app.portInput, '8000')
    assert app.portInput.text() == "5741"


def test_maintenance_button_server_off(app):
    app.maintenance.click()
    assert app.maintenance.isChecked() is False


def test_maintenance_button_server_on(app):
    app.startButton.click()
    app.maintenance.click()
    assert app.maintenance.isChecked() is True
    app.maintenance.click()
    assert app.maintenance.isChecked() is False


def test_stop_button_server_off(app):
    assert app.stopButton.styleSheet() == "background-color : grey"


def test_stop_button_on(app):
    app.startButton.click()
    assert app.stopButton.styleSheet() == "background-color : #fc4503"
    app.stopButton.click()
    assert app.stopButton.styleSheet() == "background-color : grey"


def test_start_button_server_off(app):
    assert app.startButton.styleSheet() == "background-color : green"


def test_start_button_server_on(app):
    app.startButton.click()
    assert app.startButton.styleSheet() == "background-color : yellow"
