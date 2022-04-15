import json

# create result's file to write the answer
outfile = open("result1.csv", 'w')

# object_result = {nomor / email / orderId: { id: id_value, ticket_trace: pair_id_value, contacts: jumlah_contact_value } } 

# {'Id': 0, 'Email': 'gkzAbIy@qq.com', 'Phone': '', 'Contacts': 1, 'OrderId': '', simmilar_value: [Email/OrderId/Phone]}
object_result = {}
with open('contacts.json', "r") as infile:
    contact_json = json.load(infile)
    for value in contact_json:
        if (value['Email'] != ''):
            if (value['Email'] in object_result):
                object_result[value['Email']]['ticket_trace'] += '-' + str(value['Id'])
                object_result[value['Email']]['list_ticket_trace'].append(str(value['Id']))
                object_result[value['Email']]['contacts'] = str(int(object_result[value['Email']]['contacts']) + value['Contacts'])
            else:
                object_result[value['Email']] = {}
                object_result[value['Email']]['ticket_trace'] = str(value['Id'])
                object_result[value['Email']]['list_ticket_trace'] = [str(value['Id'])]
                object_result[value['Email']]['contacts'] = str(value['Contacts'])
        if (value['Phone'] != ''):
            if (value['Phone'] in object_result):
                object_result[value['Phone']]['ticket_trace'] += '-' + str(value['Id'])
                object_result[value['Phone']]['list_ticket_trace'].append(str(value['Id']))
                object_result[value['Phone']]['contacts'] = str(int(object_result[value['Phone']]['contacts']) + value['Contacts'])
            else:
                object_result[value['Phone']] = {}
                object_result[value['Phone']]['ticket_trace'] = str(value['Id'])
                object_result[value['Phone']]['list_ticket_trace'] = [str(value['Id'])]
                object_result[value['Phone']]['contacts'] = str(value['Contacts'])
        if (value['OrderId'] != ''):
            if (value['OrderId'] in object_result):
                object_result[value['OrderId']]['ticket_trace'] += '-' + str(value['Id'])
                object_result[value['OrderId']]['list_ticket_trace'].append(str(value['Id']))
                object_result[value['OrderId']]['contacts'] = str(int(object_result[value['OrderId']]['contacts']) + value['Contacts'])
            else:
                object_result[value['OrderId']] = {}
                object_result[value['OrderId']]['ticket_trace'] = str(value['Id'])
                object_result[value['OrderId']]['list_ticket_trace'] = [str(value['Id'])]
                object_result[value['OrderId']]['contacts'] = str(value['Contacts'])

# write header of csv output
outfile_header = "ticked_id,ticket_trace/contact\n"
outfile.write(outfile_header)

dictionary_result = {}
for _, value in object_result.items():
    for id_user in value['list_ticket_trace']:
        str_concat = value['ticket_trace']+ ', '+value['contacts']
        if id_user not in dictionary_result:
            dictionary_result[int(id_user)] = str_concat

for value in sorted(dictionary_result):
    line = "{},{}\n".format(str(value), dictionary_result[value])
    outfile.write(line)
outfile.close()

