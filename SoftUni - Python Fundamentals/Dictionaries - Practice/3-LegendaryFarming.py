materials_dict = {}
while True:
    materials = input().split()
    for index in range(len(materials)):
        if index % 2 != 0:
            if materials[index].lower() not in materials_dict:
                materials_dict[materials[index].lower()] = int(materials[index - 1])
            else:
                materials_dict[materials[index].lower()] += int(materials[index - 1])
    if 'shards' in materials_dict:
        if materials_dict['shards'] >= 250:
            print('Shadowmourne obtained!')
            break
    if 'fragments' in materials_dict:
        if int(materials_dict['fragments']) >= 250:
            print('Valanyr obtained!')
            break
    if 'motes' in materials_dict:
        if materials_dict['motes'] >= 250:
            print('Dragonwrath obtained!')
            break

sorted(materials_dict)

print(materials_dict)