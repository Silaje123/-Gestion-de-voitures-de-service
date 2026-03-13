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

class Voiture:

    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformations(self):

        print("Matricule:", self.matricule)
        print("Marque:", self.marque)
        print("Année:", self.annee)
        print("Kilometrage:", self.kilometrage)

        if self.chauffeur:
            print("Chauffeur:", self.chauffeur.nom, self.chauffeur.prenom)
        else:
            print("Aucun chauffeur")

v1 = Voiture("A123", 2020, "Toyota", 50000)
v2 = Voiture("B456", 2021, "Honda", 30000)
v3 = Voiture("C789", 2019, "BMW", 70000)

e1 = Employe("P111", "Michel", "Silaje")
e2 = Employe("P222", "Marie", "Claire")
e3 = Employe("P333", "Jean", "Paul")

print("---Employés---")
e1.afficherInformations()
e2.afficherInformations()
e3.afficherInformations()

print("---Voitures---")
v1.afficherInformations()
v2.afficherInformations()
v3.afficherInformations()


print("---affectation---")

e1.affecterVoiture(v1)
e2.affecterVoiture(v2)

e1.afficherInformations()
e2.afficherInformations()

print("---Retirer voiture---")

e1.retirerVoiture()
e2.afficherInformations()

