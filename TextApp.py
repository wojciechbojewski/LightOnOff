from Logic import Logic
from ToggleSwitch import ToggleSwitch
from LightBulb import LightBulb
from ToggleSwitchTextView import ToggleSwitchTextView
from LightBulbTextView import LightBulbTextView


ts1 = ToggleSwitch()
ts2 = ToggleSwitch()
ts3 = ToggleSwitch()
lb = LightBulb()
tsv1 = ToggleSwitchTextView(ts1)
tsv2 = ToggleSwitchTextView(ts2)
tsv3 = ToggleSwitchTextView(ts3)
lbv = LightBulbTextView(lb)
logic = Logic(lb, [ts1, ts2, ts3])

while True:

    command = input("> ")
    match command.split(" "):
        case ["quit"] | ["exit"]:
            break
        case ["show"]:
            logic.processing()
            tsv1.view()
            tsv2.view()
            tsv3.view()
            lbv.view()
        case ["switch", name]:
            match name:
                case "ts1":
                    ts1.switch()
                case "ts2":
                    ts2.switch()
                case "ts3":
                    ts3.switch()
                case _:
                    print("Unknown ToggleSwitch")
        case _:
            print(f"Unknown command {command}")
            print()
            print("show - print state of elements")
            print("switch [TOGGLESWITCH]")
            print("exit or quit to close application")
