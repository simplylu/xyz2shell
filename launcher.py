import subprocess
import argparse
import sys

description = "This is xyz2shell, a list of very dangerous CVSS 13.37 vulnerabilities."
epilog = "Many programming if not all languages are affected. Fix these A.S.A.P or you'll be hacked."

def hi():
    print("                                ______             __                  __  __ ")
    print("                               /      \\           /  |                /  |/  |")
    print(" __    __  __    __  ________ /$$$$$$  |  _______ $$ |____    ______  $$ |$$ |")
    print("/  \\  /  |/  |  /  |/        |$$____$$ | /       |$$      \\  /      \\ $$ |$$ |")
    print("$$  \\/$$/ $$ |  $$ |$$$$$$$$/  /    $$/ /$$$$$$$/ $$$$$$$  |/$$$$$$  |$$ |$$ |")
    print(" $$  $$<  $$ |  $$ |  /  $$/  /$$$$$$/  $$      \\ $$ |  $$ |$$    $$ |$$ |$$ |")
    print(" /$$$$  \\ $$ \\__$$ | /$$$$/__ $$ |_____  $$$$$$  |$$ |  $$ |$$$$$$$$/ $$ |$$ |")
    print("/$$/ $$  |$$    $$ |/$$      |$$       |/     $$/ $$ |  $$ |$$       |$$ |$$ |")
    print("$$/   $$/  $$$$$$$ |$$$$$$$$/ $$$$$$$$/ $$$$$$$/  $$/   $$/  $$$$$$$/ $$/ $$/ ")
    print("          /  \\__$$ |                                                          ")
    print("          $$    $$/                                                           ")
    print("           $$$$$$/                                                            ")
    print()

def lucky(ext: str) -> None:
    print(f"You're lucky this time, you're not vulnerable to {ext}2shell")

def is_exploitable(launcher: str) -> bool:
    try:
        subprocess.check_output(["which", launcher])
        return True
    except subprocess.CalledProcessError:
        return False

def run_exploit(launcher: str, ext: str) -> None:
    if not is_exploitable(launcher):
        lucky(ext)
    try:
        subprocess.run(f"{launcher} exploits/shell.{ext}", shell=True)
    except:
        print("Exiting gracefully...")
        sys.exit(420)

def compile_run_exploit(ext: str) -> None:
    if ext == "c":
        if not is_exploitable("gcc"):
            lucky(ext)
        subprocess.run("gcc -O2 -Wall -Wextra ./exploits/shell.c -o ./exploits/c2shell && ./exploits/c2shell", shell=True)
    elif ext == "cpp":
        if not is_exploitable("g++"):
            lucky(ext)
        subprocess.run("g++ -std=c++17 -O2 -Wall -Wextra ./exploits/shell.cpp -o ./exploits/cpp2shell && ./exploits/cpp2shell", shell=True)
    elif ext == "rs":
        if not is_exploitable("rustc"):
            lucky(ext)
        subprocess.run("rustc -O ./exploits/shell.rs -o ./exploits/rs2shell && ./exploits/rs2shell", shell=True)

def main():
    hi()
    ap = argparse.ArgumentParser(description=description, epilog=epilog)
    ap.add_argument("--python", action="store_true", help="Launches py2shell exploit")
    ap.add_argument("--bash", action="store_true", help="Launches sh2shell exploit")
    ap.add_argument("--node", action="store_true", help="Launches node2shell (v2) exploit")
    ap.add_argument("--c", action="store_true", help="Launches c2shell exploit")
    ap.add_argument("--cpp", action="store_true", help="Launches cpp2shell exploit")
    ap.add_argument("--rust", action="store_true", help="Launches rs2shell exploit")
    ap.add_argument("--ruby", action="store_true", help="Launches rb2shell exploit")
    ap.add_argument("--cmd", action="store_true", help="Launches cmd2shell exploit")
    ap.add_argument("--powershell", action="store_true", help="Launches ps2shell exploit")
    ap.add_argument("--x420", nargs="+", help="Secret, don't be afraid of exceptions.")

    args = ap.parse_args()
    if args.python:
        run_exploit(launcher="python3", ext="py")
    elif args.bash:
        run_exploit(launcher="bash", ext="sh")
    elif args.node:
        run_exploit(launcher="node", ext="js")
    elif args.ruby:
        run_exploit(launcher="ruby", ext="rb")
    elif args.cmd:
        run_exploit(launcher="cmd.exe", ext="rb")
    elif args.powershell:
        run_exploit(launcher="powershell", ext="rb")
    elif args.c:
        compile_run_exploit("c")
    elif args.cpp:
        compile_run_exploit("cpp")
    elif args.rust:
        compile_run_exploit("rs")
    elif args.x420:
        run_exploit(launcher="bash", ext="".join(sys.argv).split("--x420")[-1])
    else:
        ap.print_help()


if __name__ == "__main__":
    main()