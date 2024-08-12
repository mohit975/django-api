import subprocess

def create_directory(command):
  escaped_command = command.replace("\\", "\\\\")  # Escape backslashes for shell interpretation
  subprocess.run(escaped_command, shell=True)

if __name__ == "__main__":
  command = "mkdir -p C:\\Users\\acer\\Desktop\\Github\\GK-KT\\api\\xyz"
  create_directory(command)