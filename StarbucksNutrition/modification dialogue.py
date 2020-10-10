IngCt = {}


mocha_preset = input('Do you want a grande mocha?: ')
if mocha_preset in ['y', 'yes', 'sure', 'sure do', 'i do', 'yep', 'absolutely']:
    IngCt['pumps of mocha'] = 4
    IngCt['shots of signature espresso'] = 2
    IngCt['serving of whipped cream'] = 1
else:


q_modify = input('Do you want to modify your drink?: ')
loop_mod = True
if q_modify.lower in ['y', 'yes', 'sure', 'sure do', 'i do', 'yep', 'absolutely']:
    while loop_mod:
        q_mod_method = input('What part of your drink do you want to change?: ')
        if q_mod_method.lower in ['syrup', 'the syrup', 'syrups', 'the syrups', 'flavor', 'the flavor', 'flavors', 'the flavors',]:
            loop_syr_mod = True
            while loop_syr_mod:
                q_mod_method_syr = input('Which syrup would you like to modify the amount of?: ')
                if q_mod_method_syr.lower in ['vanilla']:
                    IngCt['pumps of vanilla'] = input('How many pumps of vanilla would you like?: ')
                elif q_mod_method_syr.lower in ['toffee nut']:
                    IngCt['pumps of toffee nut'] = input('How many pumps of toffee nut would you like?: ')
                elif q_mod_method_syr.lower in ['hazelnut']:
                    count_syr_van = input('How many pumps of hazelnut would you like?: ')
                elif q_mod_method_syr.lower in ['mocha']:
                    count_sauc_mocha = input('How many pumps of mocha would you like?: ')
                elif q_mod_method_syr.lower in ['white mocha']:
                    count_sauc_wmocha = input('How many pumps of white mocha would you like?: ')
                elif q_mod_method_syr.lower in ['cinnamon', 'cinnamon dolce']:
                    count_syr_cindlc = input('How many pumps of cinnamon dolce would you like?: ')
                elif q_mod_method_syr.lower in ['']:
                    count_syr_van = input('How many pumps of vanilla would you like?: ')
                elif q_mod_method_syr.lower in ['vanilla']:
                    count_syr_van = input('How many pumps of vanilla would you like?: ')
                elif q_mod_method_syr.lower in ['hazelnut']:
                else:
                    loop_mod_syr_check('Any other changes to syrups?: ')
                    if loop_mod_syr_check.lower in ['yes']:
                        continue
                    else:
                        loop_syr_mod = False

        elif q_mod_method.lower in ['milk', 'the milk', 'milk alternatives']:
            loop_milk_mod = True
            while loop_milk_mod:
                q_mod_method_milk = input('What kind of milk would you like?: ')
                if q_mod_method_milk.lower in ['skim', 'nonfat', 'fat free']:
                    milk_type = 'nonfat'
                elif q_mod_method_milk.lower in ['two percent', '2pc', '2 percent', 'two pc', '2%']:
                    milk_type = '2pc'
                elif q_mod_method_milk.lower in []

        elif q_mod_method.lower in ['espresso', 'coffee', 'shots', 'the espresso', 'the coffee', 'the shots']:
            loop_esp_mod = True
            q_mod_method_esp = input('What do you want to change about your espresso? ')
            while loop_esp_mod:
                if q_mod_method_esp.lower in ['type', 'decaf']
                elif q_mod_method_esp.lower in ['number', 'number of shots']:
                    count_esp_sig = input('How many shots of espresso would you like?: ')
        elif q_mod_method.lower in ['whip', 'whipped cream']:
            loop_topp_mod = True
            while loop_topp_mod:
                q_mod_method_whip = input('Do you want whipped cream on that?: ')
                if q_mod_method_whip in ['y', 'yes', 'sure', 'sure do', 'i do', 'yep', 'absolutely']:
                    IngCt['serving of whipped cream'] = 1
                elif q_mod_method_whip in ['no']:
                    IngCt['serving of whipped cream'] = 0
                else:
                    loop_topp_mod = False




        else:
            print('These are acceptable values: Syrups, Milk, Espresso, Whip')
            print('What part of your drink do you want to change?:')

elif q_modify.lower in ['no', 'nope']:
    loop_mod = False
    print('Okay, let\'s move on then')

print('your drink has ')


str_end = ''.join(f'{val} {key}, ' for key, val in IngCt.items() if val != 0)
print(f'Your drink contains {str_end}')