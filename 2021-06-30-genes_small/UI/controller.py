import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        nodi = self._model.getNodes()
        for n in nodi:
            self._view.txtInLocalizzazione.options.append(ft.dropdown.Option(n))

    def handle_graph(self):
        grafo = self._model.buildGraph()
        self._view.txt_result.controls.clear()
        if grafo:
            self._view.txt_result.controls.append(ft.Text(f"Grafo creato: {self._model.printGraphDetails()}"))
            self.fillDD()
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text("Errore nella creazione del grafo!", color='red'))
            self._view.update_page()
            return

    def handle_statistiche(self, e):
        l = self._view.txtInLocalizzazione.value
        if l is None:
            self._view.txt_result.controls.append(ft.Text("Seleziona una localizzazione!"))
            self._view.update_page()
            return
        else:
            mappa = self._model.compConn(l)
            self._view.txt_result.controls.append(ft.Text(f"Adiacenti a: {l}"))
            for k, v in mappa.items():
                self._view.txt_result.controls.append(ft.Text(f"{k} {v}"))
            self._view.update_page()

    def handle_cromosomi(self, e):
        pass
