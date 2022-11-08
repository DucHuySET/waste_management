import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    width: 1920
    height: 1080
    visible: true
    title: qsTr("Waste Management")
    visibility: Qt.WindowFullScreen
    Rectangle {
        width: Constants.width
        height: Constants.height
        border.width: 0
        color: "white"

        Rectangle {
            width: 1920
            height: 1080
            border.width: 0
            color: "#ccf5ff"
        }

        Button {
            id: iconImport
            x: 70
            y: 30
            icon.name: "import"
            icon.source: "assets/icons/baseline_download_black_24dp.png"
            icon.width: 50
            icon.height: 50
            icon.color: "#3388ea"
            background: Rectangle {
                width: 100
                height: 100
                radius: myRoundButton.radius
                color: "#0000ffff"
            }
        }

        Text {
            id: text1
            x: 150
            y: 30
            width: 498
            height: 48
            color: "#222222"
            text: qsTr("Thông tin nhập phế liệu")
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
                    x: 65
                    y: 5
                    width: 200
                    height: 70
                    text: "Nhân viên cân đầu vào"
                    font.pixelSize: 32
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
                property bool isChoose: false

                TextInput {
                    id: textInput
                    x: 23
                    y: 28
                    width: 478
                    height: 35
                    text: qsTr("")
                    font.pixelSize: 26
                    focus: true
                    maximumLength: 50
                    onFocusChanged: {
                    }
                    onEditingFinished: {
                        textInput1.focus = true
                    }
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
                    y: 5
                    width: 287
                    height: 70
                    text: "Nhân viên tập kết phế liệu"
                    font.pixelSize: 30
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
                TextInput {
                    id: textInput3
                    x: 23
                    y: 28
                    width: 478
                    height: 35
                    text: qsTr("")
                    font.pixelSize: 26
                    onEditingFinished: {
                        textInput4.focus = true
                    }

                }
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
                TextInput {
                    id: textInput4
                    x: 23
                    y: 28
                    width: 478
                    height: 35
                    text: qsTr("")
                    font.pixelSize: 26
                    maximumLength: 50
                    onEditingFinished: textInput5.focus = true
                }
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
                TextInput {
                    id: textInput1
                    x: 23
                    y: 28
                    width: 478
                    height: 35
                    text: qsTr("")
                    font.pixelSize: 26
                    maximumLength: 50
                    onEditingFinished: textInput2.focus = true
                }
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
                TextInput {
                    id: textInput2
                    x: 23
                    y: 28
                    width: 478
                    height: 35
                    text: qsTr("")
                    font.pixelSize: 26
                    maximumLength: 50
                    onEditingFinished: textInput3.focus = true
                }
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
                TextInput {
                    id: textInput5
                    x: 23
                    y: 28
                    width: 478
                    height: 35
                    text: qsTr("")
                    font.pixelSize: 26
                    maximumLength: 50
                    onEditingFinished: textInput6.focus = true
                }
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
                TextInput {
                    id: textInput6
                    x: 23
                    y: 28
                    width: 478
                    height: 35
                    text: qsTr("")
                    font.pixelSize: 26
                    maximumLength: 50
                    onEditingFinished: textInput7.focus = true
                }
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

//            CheckBox {
//                id: checkBox
//                x: 546
//                y: 617
//                width: 61
//                height: 63
//                text: qsTr("Check Box")
//            }

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
                TextInput {
                    id: textInput7
                    x: 23
                    y: 28
                    width: 478
                    height: 35
                    text: qsTr("")
                    font.pixelSize: 26
                    maximumLength: 50
                    onEditingFinished: textInput8.focus = true
                }
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
//            DropShadow {
//                id: rectShadow2
//                color: "#505050"
//                radius: 8
//                anchors.fill: source
//                source: container
//                verticalOffset: 10
//                cached: true
//                horizontalOffset: 10
//                samples: 16
//                smooth: true
//            }

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

        Rectangle {
            id: rectangle25
            x: 1240
            y: 850
            width: 100
            height: 50
            color: "#4a8cd7"
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

}
