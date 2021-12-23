def get_DNAs(quantity_of_dna:int, 
            quantity_of_nucleotides:int) -> list:
    
    from random import choice
   
    def get_dna(quantity_of_nucleotides):
        string = ''
        for i in range(quantity_of_nucleotides):
            string += choice('ATGC')
        return string
    
    def stat(string, DNA):
        counter = 0
        if type(DNA) == str:
            for i in range(len(DNA)):
                if DNA[i] == string:
                    counter +=1
        else:
            for i in DNA:
                for k in range(len(i)):
                    if i[k] == string:
                        counter += 1
        return counter
    
    list_DNAs = []
    for i in range(quantity_of_dna):
        list_DNAs.append(get_dna(quantity_of_nucleotides))
        
    C_quanity = stat('C', list_DNAs)
    A_quanity = stat('A', list_DNAs)
    T_quanity = stat('T', list_DNAs)
    G_quanity = stat('G', list_DNAs)
    
    C_stat = C_quanity / (C_quanity + A_quanity + T_quanity + G_quanity)
    A_stat = A_quanity / (C_quanity + A_quanity + T_quanity + G_quanity)
    T_stat = T_quanity / (C_quanity + A_quanity + T_quanity + G_quanity)
    G_stat = G_quanity / (C_quanity + A_quanity + T_quanity + G_quanity)
    GC_stat = (G_quanity + C_quanity) / (C_quanity + A_quanity + T_quanity + G_quanity)
    
    print('ДНК-последовательности')
    a = 1
    for i in list_DNAs:
        print(f"{a}. {i}")
        print(f"Доля нуклеотидов С - {(stat('C', i) + stat('G', i)) / (2 * len(i))}")
        print(f"Доля нуклеотидов A - {(stat('A', i) + stat('T', i)) / (2 * len(i))}")
        print(f"Доля нуклеотидов T - {(stat('A', i) + stat('T', i)) / (2 * len(i))}")
        print(f"Доля нуклеотидов G - {(stat('C', i) + stat('G', i)) / (2 * len(i))}")
        print(f"GC-cостав - {(stat('C', i) + stat('G', i)) / len(i)}")
        print('__________________\n')
        a += 1
    
    print(f'Общяя доля Цитозина - {(C_stat + G_stat) / 2}')
    print(f'Общяя доля Аденина - {(A_stat + T_stat) / 2}')
    print(f'Общяя доля Тимина - {(A_stat + T_stat) / 2}')
    print(f'Общяя доля Гуанина - {(C_stat + G_stat) / 2}')
    print(f'GC-состав - {GC_stat*100}%')
    
    return list_DNAs
    
