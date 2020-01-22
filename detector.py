
import os, zipfile, json

def get_mod_list(dir_path):
    result = {}
    for name in os.listdir(dir_path):
        file = zipfile.Zipfile(os.path.join(dir_path, name))
        json_string = file.read("mcmod.info")
        json_obj = json.loads(json_string)
        for modinfo in json_obj:
            modid = modinfo.get("modid")
            version = modinfo.get("version")
            if modid not in result.keys():
               result[modid] = {}
            if version not in result[modid].keys():
                result[modid][version] = []
            result[modid][version].append(os.path.join(dir_path, name))
    return result     
            
