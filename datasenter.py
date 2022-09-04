from regneklynge import Regneklynge
from node import Node

## Klasse for representasjon av et datasenter
#
class Datasenter:

    ## Oppretter et datasenter
    #
    def __init__(self):
        self._regneklynger = {}

    ## Leser inn data om en regneklynge fra fil og legger
    # den til i ordboken
    # @param filnavn filene der dataene for regneklyngen ligger
    def lesInnRegneklynge(self, filnavn):
        regneklynge = open(filnavn)
        klyngenavn = filnavn.strip().split(".txt")[0]
        for linje in regneklynge:
            linjedeler = linje.strip().split()
            if len(linjedeler) == 1:
                maksNoderPerRack = int(linjedeler[0])
                self._regneklynger[klyngenavn] = Regneklynge(maksNoderPerRack)
            else:
                antallNoder = int(linjedeler[0])
                minnePerNode = int(linjedeler[1])
                antProsPerNode = int(linjedeler[2])
                for klyngeNode in range(antallNoder):
                    nyNode = Node(minnePerNode, antProsPerNode)
                    self._regneklynger[klyngenavn].settInnNode(nyNode)

    # Hjelpemetode for å hente ut informasjon om regneklynge
    def _infoOmRegneklynge(self, navn, klynge):
        print()
        print(f"Informasjon om regneklyngen {navn}: ")
        print(f"Antall racks: {klynge.antRacks()}")
        print(f"Antall prosessorer: {klynge.antProsessorer()}")
        print(f"Noder med minst 32 GB: {klynge.noderMedNokMinne(32)}")
        print(f"Noder med minst 64 GB: {klynge.noderMedNokMinne(64)}")
        print(f"Noder med minst 128 GB: {klynge.noderMedNokMinne(128)}")
        print()

    ## Skriver ut informasjon om alle regneklyngene
    #
    def skrivUtAlleRegneklynger(self):
        for navn, klynge in self._regneklynger.items():
            self._infoOmRegneklynge(navn, klynge)

    ## Skriver ut informasjon om en spesifikk regneklynge
    # @param navn navnet på regnekyngen
    def skrivUtRegneklynge(self, navn):
        klynge = self._regneklynger[navn.lower()]
        self._infoOmRegneklynge(navn, klynge)
