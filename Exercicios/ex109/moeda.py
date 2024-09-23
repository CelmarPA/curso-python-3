def metade(val=0, fmt=False):
    """
    -> Função para calcular a metade de um valor
    :param val: Valor a que se deseja alterar
    :param fmt: Parâmentro opcional para formatar o valor inserido
    :return: Retorna a metade do valor inserido
    """
    valor = val / 2
    if fmt is True:
        return moeda(valor)
    else:
        return valor


def dobro(val=0, fmt=False):
    """
        -> Função para calcular o dobro de um valor
        :param val: Valor a que se deseja alterar
        :param fmt: Parâmentro opcional para formatar o valor inserido
        :return: Retorna ao dobro do valor inserido
        """
    valor = val * 2
    if fmt is True:
        return moeda(valor)
    else:
        return valor


def aumentar(val=0, por=0, fmt=False):
    """
    -> Função para calcular aumento percentual de um valor
    :param val: Valor a que se deseja aplicar o aumento
    :param por: Porcentagem de aumento
    :param fmt: Parâmentro opcional para formatar o valor inserido
    :return: Returna o valor com aumento indicado pelo parâmetro por
    """
    valor = (val + (val * por / 100))
    if fmt is True:
        return moeda(valor)
    else:
        return valor


def diminuir(val=0, por=0, fmt=False):
    """
        -> Função para calcular redução percentual de um valor
        :param val: Valor a que se deseja aplicar a redução
        :param por: Porcentagem de redução
        :param fmt: Parâmentro opcional para formatar o valor inserido
        :return: Returna o valor com redução indicada pelo parâmetro por
        """
    valor = (val - (val * por / 100))
    if fmt is True:
        return moeda(valor)
    else:
        return valor


def moeda(val=0.0, sifra='R$'):
    """
    -> Função para formatação de um valor para valor monetário
    :param val: Valor a que se deseja formatar
    :param sifra: Sifra da moeda desejada
    :return: Returna um valor monetário de um valor normal inserido
    """
    return f'{sifra}{val:.2f}'.replace('.', ',')
