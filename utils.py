import pandas as pd

def formatar_moeda_br(df, coluna):
    """
    Recebe um DataFrame e o nome de uma coluna numérica.
    Retorna uma Series formatada como R$ 1.234,56.
    """
    # 1. Multiplica e arredonda
    serie_aux = (df[coluna] * 1000).round(2)
    
    # 2. Aplica a formatação de string
    # Usamos o padrão :_ que coloca sublinhado como milhar, depois trocamos
    return serie_aux.apply(
        lambda x: f"R$ {x:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

# Exemplo de uso:
# df['Impostos_text'] = formatar_moeda_br(df, 'Impostos')
# df['vab_bruto_text'] = formatar_moeda_br(df, 'vab_bruto')