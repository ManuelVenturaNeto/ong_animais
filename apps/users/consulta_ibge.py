from ibge.localidades import *


def unidade_federativa():
    uf_estado = Estados()
    sigla_uf = uf_estado.getSigla()
    return sigla_uf


def municipios_por_uf(unidade_federativa):    
    estado_por_uf = MunicipioPorUF(unidade_federativa)
    nome_municipios = estado_por_uf.getNome()
    return nome_municipios
