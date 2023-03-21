import json

def create_lists(df):
    llistes = [
        # Llista Nacional:
        {
            'id': 'recJeO0Mu4TSk8SPf',
            'fields': {
                'votes': int(df.iloc[2,3] + df.iloc[13,3] + df.iloc[25, 3] + df.iloc[38, 3] + df.iloc[51,3] + df.iloc[65,3] + df.iloc[79, 3])
            } # DA
        },
        {
            'id': 'recX9CRRFH9yLkBFR',
            'fields': {
                'votes': int(df.iloc[5,3] + df.iloc[16,3] + df.iloc[28, 3] + df.iloc[41, 3] + df.iloc[54,3] + df.iloc[68,3] + df.iloc[82, 3])
            } # PS
        },
        {
            'id': 'reckf2p3g2kcsJ4IZ',
            'fields': {
                'votes': int(df.iloc[0,3] + df.iloc[11,3] + df.iloc[23, 3] + df.iloc[36, 3] + df.iloc[49,3] + df.iloc[63,3] + df.iloc[77, 3])
            } # Liberals
        },
        {
            'id': 'reca2Qzjta3qg5qkG',
            'fields': {
                'votes': int(df.iloc[3,3] + df.iloc[14,3] + df.iloc[26, 3] + df.iloc[39, 3] + df.iloc[52,3] + df.iloc[66,3] + df.iloc[80, 3])
            } # Acció
        },
        {
            'id': 'recVi8I4tKcOL195J',
            'fields': {
                'votes': int(df.iloc[4,3] + df.iloc[15,3] + df.iloc[27, 3] + df.iloc[40, 3] + df.iloc[53,3] + df.iloc[67,3] + df.iloc[81, 3])
            } # Endavant
        },
        {
            'id': 'recJFqscvqla4hWmn',
            'fields': {
                'votes': int(df.iloc[1,3] + df.iloc[12,3] + df.iloc[24, 3] + df.iloc[37, 3] + df.iloc[50,3] + df.iloc[64,3] + df.iloc[78, 3])
            } # Concòrdia
        },

        # Llista Canillo:
        {
            'id': 'recuZj5NleyPBOwFS',
            'fields': {
                'votes': int(df.iloc[8,3])
            } # DA
        },

        # Llista Encamp:
        {
            'id': 'recq1huYYFiVSUvlO',
            'fields': {
                'votes': int(df.iloc[19,3])
            } # PS
        },
        {
            'id': 'recx8UlOslG8DMFjd',
            'fields': {
                'votes': int(df.iloc[20,3])
            } # DA
        },

        # Llista Ordino:
        {
            'id': 'recpZRAwTHN56Sno1',
            'fields': {
                'votes': int(df.iloc[32,3])
            } # DA
        },
        {
            'id': 'reciZPMzJRNPWFtkm',
            'fields': {
                'votes': int(df.iloc[33,3])
            } # Endavant
        },
        {
            'id': 'recUpCyxtyCeBen2H',
            'fields': {
                'votes': int(df.iloc[31,3])
            } # PS
        },

        # LLista Massana:
        {
            'id': 'rec29GlXXkvxB78kF',
            'fields': {
                'votes': int(df.iloc[45,3])
            } # DA
        },
        {
            'id': 'recPW2138OYL6kckJ',
            'fields': {
                'votes': int(df.iloc[44,3])
            } # PS
        },
        {
            'id': 'rectdl10pE4GfFAYk',
            'fields': {
                'votes': int(df.iloc[46,3])
            } # Acció
        },

        # Llista Andorra:
        {
            'id': 'recEQMEpV19eTugiY',
            'fields': {
                'votes': int(df.iloc[58,3])
            } # DA
        },
        {
            'id': 'recJe7rA61BCrgSaa',
            'fields': {
                'votes': int(df.iloc[59,3])
            } # PS
        },
        {
            'id': 'recBqazmfwovNXE0l',
            'fields': {
                'votes': int(df.iloc[57,3])
            } # Concòrdia
        },
        {
            'id': 'recOsly6lLoKoBbEr',
            'fields': {
                'votes': int(df.iloc[60,3])
            } # Endavant
        },

        # Llista StJu:
        {
            'id': 'recGm4C2yrXdjticw',
            'fields': {
                'votes': int(df.iloc[72,3])
            } # Endavant
        },
        {
            'id': 'recGgPJ0EcbtyT9k1',
            'fields': {
                'votes': int(df.iloc[71,3])
            } # PS
        },
        {
            'id': 'recslIrVrRRx8AuDM',
            'fields': {
                'votes': int(df.iloc[73,3])
            } # Concòrdia
        },
        {
            'id': 'recbodeJQrjUPKiNU',
            'fields': {
                'votes': int(df.iloc[74,3])
            } # DA
        },

        # Llista Escaldes:
        {
            'id': 'recUvJudzNRNFgSRm',
            'fields': {
                'votes': int(df.iloc[86,3]) 
            } # DA
        },
        {
            'id': 'rec5ndckdwnntcKcn',
            'fields': {
                'votes': int(df.iloc[87,3])
            } # PS
        },
        {
            'id': 'rec0VLpjPRW2yDCw4',
            'fields': {
                'votes': int(df.iloc[85,3])
            } # Concòrdia
        },
    ]

    return (llistes)