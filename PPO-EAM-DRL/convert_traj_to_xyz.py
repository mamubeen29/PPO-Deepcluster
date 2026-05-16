import os
import shutil
from ase.io import read, write

def convert_and_move_traj_files(input_directory, output_directory):
    """
    将指定目录下的所有`.traj`文件转换为`.xyz`文件，并移动到输出目录。
    
    参数:
    input_directory: 包含`.traj`文件的目录路径
    output_directory: 输出 `.xyz` 文件的目录路径
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".traj"):
                traj_path = os.path.join(root, file)
                xyz_filename = os.path.splitext(file)[0] + ".xyz"
                xyz_path = os.path.join(output_directory, xyz_filename)
                
                # 读取 .traj 文件
                traj = read(traj_path, index=':')
                
                # 写入 .xyz 文件
                write(xyz_path, traj)
                print(f"Converted {traj_path} to {xyz_path}")

if __name__ == "__main__":
    # 当前目录
    current_directory = os.getcwd()
    
    # 名为 "trajs" 的子文件夹路径
    trajs_directory = os.path.join(current_directory, 'trajs')
    
    # 新建的 "xyz" 文件夹路径
    xyz_directory = os.path.join(current_directory, 'xyz')
    
    # 检查 "trajs" 文件夹是否存在
    if os.path.exists(trajs_directory):
        convert_and_move_traj_files(trajs_directory, xyz_directory)
    else:
        print(f"Directory {trajs_directory} does not exist.")
