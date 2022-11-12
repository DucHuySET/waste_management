import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "./import_screen.qml" as importScreens

Window {
    width: 1920
    height: 1080
    visible: true
    title: qsTr("Waste Management")
    visibility: Qt.WindowFullScreen

    StackView{
        id: stackview
        width: implicitWidth
        height: implicitHeight
        initialItem: Component {
            id: firstPage
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
                Button{
                    id: goToScreenImport
                    x: 600
                    y: 400
                    text: qsTr("Lưu")
                    width: 300
                    height: 300
                    onClicked: {
                        stackview.replace(importScreen)
                    }
                }
                Button{
                    id: goToScreenExport
                    x: 1000
                    y: 400
                    text: qsTr("Lưu")
                    width: 300
                    height: 300
                }

            }

        }
        //import_screen {}
    }
}
