

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import Waste_Mafnagement 1.0

Rectangle {
    width: Constants.width
    height: Constants.height
    color: "#dae4f0"
    border.width: 0

    Text {
        id: text1
        x: 70
        y: 30
        width: 498
        height: 48
        color: "#222222"
        text: qsTr("Thông tin lượt cân")
        font.pixelSize: 41
        font.styleName: "Bold"
        font.family: "Arial"
    }

    Rectangle {
        id: rectangle
        x: 70
        y: 90
        width: 1750
        height: 3
        color: "#3388ea"
        border.color: "#ffffff"
        border.width: 0
        clip: true
    }

    Rectangle {
        id: rectangle1
        x: 70
        y: 140
        width: 1090
        height: 800
        color: "#ffffff"
        radius: 20
        border.color: "#c6c6c6"
        border.width: 1

        DropShadow {
            id: rectShadow1
            anchors.fill: source
            cached: true
            horizontalOffset: 10
            verticalOffset: 10
            radius: 8.0
            samples: 16
            color: "#505050"
            smooth: true
            source: container
        }

        Rectangle {
            id: rectangle3
            x: 60
            y: 40
            width: 330
            height: 90
            color: "#d5f2ff"
            radius: 20
            border.color: "#3388ea"
            border.width: 2
            antialiasing: true

            Text {
                id: text2
                x: 22
                y: 10
                width: 287
                height: 70
                text: "Nhân viên phụ trách cân đầu vào"
                font.pixelSize: 27
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.WordWrap
                font.styleName: "Bold"
                font.family: "Be Vietnam Pro"
                textFormat: Text.RichText
            }
        }

        Rectangle {
            id: rectangle4
            x: 442
            y: 40
            width: 524
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#3388ea"
            border.width: 2

            TextInput {
                id: textInput
                x: 23
                y: 28
                width: 478
                height: 35
                text: qsTr("|")
                font.pixelSize: 26
            }
        }

        Rectangle {
            id: rectangle5
            x: 60
            y: 170
            width: 330
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            Text {
                id: text3
                x: 22
                y: 10
                width: 287
                height: 70
                text: "Nhân viên phụ trách Tập kết phế liệu"
                font.pixelSize: 27
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.WordWrap
                font.styleName: "Bold"
                font.family: "Be Vietnam Pro"
                textFormat: Text.RichText
            }
            antialiasing: true
        }

        Rectangle {
            id: rectangle6
            x: 442
            y: 303
            width: 297
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            antialiasing: true
        }

        Rectangle {
            id: rectangle7
            x: 756
            y: 303
            width: 210
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            antialiasing: true
        }

        Rectangle {
            id: rectangle8
            x: 60
            y: 303
            width: 330
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            Text {
                id: text4
                x: 22
                y: 10
                width: 287
                height: 70
                text: "Thùng bì"
                font.pixelSize: 27
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.WordWrap
                font.styleName: "Bold"
                textFormat: Text.RichText
                font.family: "Be Vietnam Pro"
            }
            antialiasing: true
        }

        Rectangle {
            id: rectangle9
            x: 60
            y: 435
            width: 330
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            Text {
                id: text5
                x: 22
                y: 10
                width: 287
                height: 70
                text: "Chủng loại phế liệu"
                font.pixelSize: 27
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.WordWrap
                font.styleName: "Bold"
                font.family: "Be Vietnam Pro"
                textFormat: Text.RichText
            }
            antialiasing: true
        }

        Rectangle {
            id: rectangle10
            x: 463
            y: 27
            width: 130
            height: 28
            color: "#ffffff"
            border.color: "#ffffff"
            border.width: 1

            Text {
                id: text6
                x: 8
                y: 2
                text: qsTr("Thông tin")
                font.pixelSize: 22
                font.family: "Arial"
            }
        }

        Rectangle {
            id: rectangle11
            x: 463
            y: 290
            width: 78
            height: 28
            color: "#ffffff"
            border.color: "#ffffff"
            border.width: 1
            Text {
                id: text7
                x: 8
                y: 2
                text: qsTr("Mã số")
                font.pixelSize: 22
                font.family: "Arial"
            }
        }

        Rectangle {
            id: rectangle12
            x: 780
            y: 290
            width: 130
            height: 28
            color: "#ffffff"
            border.color: "#ffffff"
            border.width: 1
            Text {
                id: text8
                x: 8
                y: 2
                text: qsTr("Khối lượng")
                font.pixelSize: 22
                font.family: "Arial"
            }
        }

        Rectangle {
            id: rectangle13
            x: 442
            y: 170
            width: 297
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            antialiasing: true
        }

        Rectangle {
            id: rectangle14
            x: 756
            y: 170
            width: 210
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            antialiasing: true
        }

        Rectangle {
            id: rectangle15
            x: 442
            y: 435
            width: 297
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            antialiasing: true
        }

        Rectangle {
            id: rectangle16
            x: 463
            y: 425
            width: 78
            height: 28
            color: "#ffffff"
            border.color: "#ffffff"
            border.width: 1
            Text {
                id: text9
                x: 8
                y: 2
                text: qsTr("Mã số")
                font.pixelSize: 22
                font.family: "Arial"
            }
        }

        Rectangle {
            id: rectangle17
            x: 756
            y: 435
            width: 210
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            antialiasing: true
        }

        Rectangle {
            id: rectangle18
            x: 780
            y: 425
            width: 105
            height: 28
            color: "#ffffff"
            border.color: "#ffffff"
            border.width: 1
            Text {
                id: text10
                x: 8
                y: 2
                text: qsTr("Tên loại")
                font.pixelSize: 22
                font.family: "Arial"
            }
        }

        Rectangle {
            id: rectangle19
            x: 186
            y: 630
            width: 204
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            Text {
                id: text11
                x: 19
                y: 8
                width: 171
                height: 70
                text: "Xác nhận cân nhập"
                font.pixelSize: 27
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.WordWrap
                font.styleName: "Bold"
                textFormat: Text.RichText
                font.family: "Be Vietnam Pro"
            }
            antialiasing: true
        }

        Rectangle {
            id: rectangle20
            x: 60
            y: 630
            width: 90
            height: 90
            color: "#ffffff"
            radius: 45
            border.width: 2
        }

        CheckBox {
            id: checkBox
            x: 546
            y: 617
            width: 61
            height: 63
            text: qsTr("Check Box")
        }

        Rectangle {
            id: rectangle21
            x: 442
            y: 630
            width: 524
            height: 90
            color: "#ffffff"
            radius: 20
            border.color: "#ebebeb"
            border.width: 2
            antialiasing: true
        }
    }

    Rectangle {
        id: rectangle2
        x: 1240
        y: 140
        width: 580
        height: 603
        color: "#ffffff"
        radius: 20
        border.color: "#c6c6c6"
        border.width: 1
        DropShadow {
            id: rectShadow2
            color: "#505050"
            radius: 8
            anchors.fill: source
            source: container
            verticalOffset: 10
            cached: true
            horizontalOffset: 10
            samples: 16
            smooth: true
        }

        Text {
            id: text12
            x: 40
            y: 30
            text: qsTr("Thông tin bản ghi")
            font.pixelSize: 35
            font.styleName: "Bold"
            font.family: "Arial"
        }

        Rectangle {
            id: rectangle22
            x: 40
            y: 85
            width: 500
            height: 3
            color: "#3388ea"
        }

        Rectangle {
            id: rectangle23
            x: 40
            y: 130
            width: 500
            height: 430
            color: "#ffffff"
            radius: 20
            border.color: "#3388ea"
            border.width: 2

            Text {
                id: text13
                x: 34
                y: 40
                width: 435
                height: 33
                text: qsTr("Chủng loại rác: ")
                font.pixelSize: 24
            }

            Text {
                id: text14
                x: 34
                y: 98
                width: 435
                height: 33
                text: qsTr("Trọng lượng rác: ")
                font.pixelSize: 24
            }

            Text {
                id: text15
                x: 34
                y: 159
                width: 435
                height: 33
                text: qsTr("Thông tin nhân viên: ")
                font.pixelSize: 24
            }

            Text {
                id: text16
                x: 34
                y: 342
                width: 435
                height: 33
                text: qsTr("Thời gian cân:")
                font.pixelSize: 24
            }

            Text {
                id: text17
                x: 102
                y: 208
                width: 367
                height: 33
                text: qsTr("Cân:")
                font.pixelSize: 24
            }

            Text {
                id: text18
                x: 102
                y: 247
                width: 367
                height: 33
                text: qsTr("Tập kết:")
                font.pixelSize: 24
            }

            Text {
                id: text19
                x: 102
                y: 286
                width: 367
                height: 33
                text: qsTr("Phân xưởng:")
                font.pixelSize: 24
            }
        }
    }

    Text {
        id: text20
        x: 1240
        y: 769
        width: 498
        height: 48
        color: "#222222"
        text: qsTr("Xác nhận")
        font.pixelSize: 41
        font.styleName: "Bold"
        font.family: "Arial"
    }

    Rectangle {
        id: rectangle24
        x: 1240
        y: 823
        width: 580
        height: 3
        color: "#3388ea"
        border.color: "#ffffff"
        border.width: 0
        clip: true
    }

    Button {
        id: button
        x: 1240
        y: 850
        width: 227
        height: 90
        text: qsTr("Lưu")
        font.pointSize: 22
        display: AbstractButton.TextOnly
    }

    Button {
        id: button1
        x: 1597
        y: 850
        width: 223
        height: 90
        opacity: 1
        text: qsTr("Hủy")
        spacing: 6
        focusPolicy: Qt.ClickFocus
        hoverEnabled: true
        enabled: true
        highlighted: false
        flat: false
        font.pointSize: 22
        checked: false
        checkable: false
        display: AbstractButton.TextOnly
    }


}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}D{i:35}D{i:42}D{i:43}D{i:44}D{i:45}D{i:46}D{i:47}D{i:48}
D{i:49}D{i:51}
}
##^##*/

