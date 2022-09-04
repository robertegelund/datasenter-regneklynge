from rack import Rack

## Klasse for representasjon av regneklynge i et datasenter.
#
class Regneklynge:
    ## Oppretter en regneklynge og setter maks antall
    # det er plass til i et rack
    # @param noderPerRack max antall noder per rack
    def __init__(self, noderPerRack):
        self._rackListe = []
        self._maksAntNoder = noderPerRack

    # Hjelpemetode for opprettelse av nytt rack, som også node legges til i
    def _leggTilRack(self, node):
        nyttRack = Rack()
        nyttRack.settInn(node)
        self._rackListe.append(nyttRack)

    ## Plasserer en node inn i et rack med ledig plass, eller i et nytt
    # @param node referanse til noden som skal settes inn i datastrukturen
    def settInnNode(self, node):
        if len(self._rackListe) > 0:
            for rackElem in self._rackListe:
                if rackElem.getAntNoder() < self._maksAntNoder:
                    rackElem.settInn(node)
                    return
        self._leggTilRack(node)

    ## Beregner totalt antall prosessorer i hele regneklyngen
    # @return totalt antall prosessorer
    def antProsessorer(self):
        antallProsessorer = 0
        for rackElem in self._rackListe:
            antallProsessorer += rackElem.antProsessorer()
        return antallProsessorer

    ## Beregner antall noder i regneklyngen med minne over angitt grense
    # @param paakrevdMinne hvor mye minne skal noder som telles med ha
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        antallNoder = 0
        for rackElem in self._rackListe:
            antallNoder += rackElem.noderMedNokMinne(paakrevdMinne)
        return antallNoder

    ## Henter antall racks i regneklyngen
    # @return antall racks
    def antRacks(self):
        return len(self._rackListe)
