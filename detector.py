
import os, zipfile, json

def get_mod_list(dir_path):
    result = {}
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)
        if os.path.isfile(path) and os.path.splitext(path)[1] == ".jar":
            file = zipfile.ZipFile(path)
            try:
                json_string = file.read("mcmod.info")
            except KeyError:
                print("No mcmod.info found in file %s" % path)
                continue
            try:
                json_obj = json.loads(json_string, strict=False, encoding='utf-8')
            except json.decoder.JSONDecodeError:
                print(json_string)
                continue
            except UnicodeDecodeError:
                print("%s contains a broken mcmod.info" % path)
                continue
            if "modList" in json_obj:
                json_obj = json_obj.get("modList")
            for modinfo in json_obj:
                modid = modinfo.get("modid")
                version = modinfo.get("version")
                if modid not in result.keys():
                   result[modid] = {}
                if version not in result[modid].keys():
                    result[modid][version] = []
                result[modid][version].append(path)
    return result     


import copy
def detect_duplication(mod_list):
    result = copy.deepcopy(mod_list)
    to_del_list = set()
    for k, v in result.items():
        if len(v.keys()) == 1:
            if len(list(v.values())[0]) == 1:
                to_del_list.add(k)
    for k in to_del_list:
        del result[k]
    return result


        
