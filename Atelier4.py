class Employee:

    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voituresService = None

    def afficherInformations(self):
        print("Employé:", self.nom, self.prenom)
        print("Permis:", self.numeroPermis)

        if self.voituresService:
            print("Voiture de service:")
            self.voituresService.afficherInformations()
        else:
            print("Aucune voiture assignée")

    def affecterVoiture(self, voiture):

        if self.voiture is not None:
            print("Cet employé a déjà une voiture.")
            return

        if voiture.chauffeur is not None:
            print("Cette voiture est déjà assignée à un autre employé.")
            return

        self.voituresService = voiture
        voiture.chauffeur = self

    def retirerVoiture(self):

        if self.voituresService is None:
            print("Aucune voiture à retirer.")
            return

        self.voituresService.chauffeur = None
        self.voitureService = None