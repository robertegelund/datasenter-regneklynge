## Klasse for representasjon av racks i en regneklynge.
#
class Rack:
    ## Oppretter et rack der det senere kan plasseres noder
    #
    def __init__(self):
        self._noder = []

    ## Plasserer en ny node inn i racket
    #  @param node noden som skal plasseres inn
    def settInn(self, node):
        self._noder.append(node)

    ## Henter antall noder i racket
    # @return antall noder
    def getAntNoder(self):
        return len(self._noder)

    ## Beregner sammenlagt antall prosessorer i nodene i et rack
    # @return antall prosessorer
    def antProsessorer(self):
        antallProsessorer = 0
        for nodeElem in self._noder:
            antallProsessorer += nodeElem.antProsessorer()
        return antallProsessorer

    ## Beregner antall noder i racket med minne over gitt grense
    # @param paakrevdMinne antall GB minne som kreves
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        antallNoder = 0
        for nodeElem in self._noder:
            if nodeElem.nokMinne(paakrevdMinne):
                antallNoder += 1
        return antallNoder
