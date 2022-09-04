from datasenter import Datasenter

# Oppretter nytt datasenter, og legger inn regneklyngene Abel og Saga
nyttDatasenter = Datasenter()
nyttDatasenter.lesInnRegneklynge("abel.txt")
nyttDatasenter.lesInnRegneklynge("saga.txt")

# Skriver ut informasjon om regneklyngene Abel og Saga
nyttDatasenter.skrivUtRegneklynge("Abel")
nyttDatasenter.skrivUtRegneklynge("Saga")
