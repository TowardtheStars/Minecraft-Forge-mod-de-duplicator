from detector import *


def kill_old(mod_list):
    conflict = detect_duplication(mod_list)
    remove_result = set()
    for modid in conflict.values():
        max_ver = max(modid.keys())
        for ver, path_list in modid.items():
            if ver != max_ver:
                for path in path_list:
                    if os.path.exists(path):
                        os.remove(path)
                        remove_result.add(path)
            else:
                if len(path_list) != 1:
                    path_list.sort(reverse=True)
                    for i in range(1, len(path_list)):
                        os.remove(path_list[i])
                        remove_result.add(path_list[i])
    return remove_result            

def main():
    import sys
    if len(sys.argv) == 2:
        mod_dir = sys.argv[1]
    else:
        mod_dir = sys.stdin.readline()[:-1]
    mod_list = get_mod_list(mod_dir)
    re = kill_old(mod_list)
    print("Removed files:")
    print(re)
        

if __name__ == "__main__":
    main()
