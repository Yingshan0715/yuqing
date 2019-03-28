import pandas as pd


def find_word(sstr, wword):
    if '_' in wword:
        return sstr.find(wword[1:])
    else:
        return sstr.find(wword)


def words_rule(wordss, dfcol):
    word_sp_col = dfcol.split('-')
    word_sp_find = [find_word(wordss, i) for i in word_sp_col]

    nn = -1
    for wor, posi in zip(word_sp_col, word_sp_find):
        if ('_' in wor) and (posi != -1):
            return 0
        elif '_' not in wor:
            if nn < posi:
                nn = posi
            else:
                return 0
    return 1


def keyword_columns(df, dfcol):
    if dfcol in df.columns:
        return df
    else:
        count_num = len(df)
        series_col = df[df.columns[0]].map(lambda x: words_rule(x, dfcol))
        df[dfcol] = series_col
        return df


if __name__ == '__main__':
    pinglun = pd.read_csv('zhengwen.csv')

    keywords = ['你', '好不好', '才没有', '人才-引进', '第-二', '券-牛奶', '盒-三']

    print(pinglun)
    for i in keywords:
        kdf = keyword_columns(pinglun, i)

    print(pinglun)

    # print(kdf.loc[kdf['盒-三']==1])
    print(kdf)
    print(kdf[kdf.columns[1:]].sum(axis=0))
