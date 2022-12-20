import pandas


def clean_genders(df):
    df.loc[df['Gender'].str.contains('male', case=False), 'Gender'] = 'male'
    df.loc[df['Gender'].str.contains('maile', case=False), 'Gender'] = 'male'
    df.loc[df['Gender'].str.contains('Man', case=False), 'Gender'] = 'male'
    df.loc[df['Gender'].str.contains('Guy', case=False), 'Gender'] = 'male'
    df.loc[df['Gender'] == 'm', 'Gender'] = 'male'
    df.loc[df['Gender'] == 'M', 'Gender'] = 'male'
    df.loc[df['Gender'] == 'Make', 'Gender'] = 'male'
    df.loc[df['Gender'] == 'msle', 'Gender'] = 'male'
    df.loc[df['Gender'] == 'Mail', 'Gender'] = 'male'
    df.loc[df['Gender'] == 'Mal', 'Gender'] = 'male'
    df.loc[df['Gender'] == 'Man', 'Gender'] = 'male'
    df.loc[df['Gender'] == 'Malr', 'Gender'] = 'male'

    df.loc[df['Gender'].str.contains('female', case=False), 'Gender'] = 'female'
    df.loc[df['Gender'] == 'f', 'Gender'] = 'female'
    df.loc[df['Gender'] == 'F', 'Gender'] = 'female'
    df.loc[df['Gender'] == 'femail', 'Gender'] = 'female'
    df.loc[df['Gender'] == 'Femake', 'Gender'] = 'female'

    df.loc[df['Gender'].str.contains('queer', case=False), 'Gender'] = 'other'
    df.loc[df['Gender'].str.contains('binary', case=False), 'Gender'] = 'other'
    df.loc[df['Gender'].str.contains('A little', case=False), 'Gender'] = 'other'
    df.loc[df['Gender'] == 'Nah', 'Gender'] = 'other'
    df.loc[df['Gender'] == 'All', 'Gender'] = 'other'
    df.loc[df['Gender'] == 'Enby', 'Gender'] = 'other'
    df.loc[df['Gender'] == 'fluid', 'Gender'] = 'other'
    df.loc[df['Gender'] == 'Agender', 'Gender'] = 'other'
    df.loc[df['Gender'] == 'Androgyne', 'Gender'] = 'other'
    df.loc[df['Gender'] == 'Neuter', 'Gender'] = 'other'
    df.loc[df['Gender'] == 'p', 'Gender'] = 'other'

    return df
