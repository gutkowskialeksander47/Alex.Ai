# team_huawei.py
"""
Projekt: TeamHuawei 2004 – Rajca
Certyfikat Autentyczności

Opis:
Skrypt prezentuje zespół TeamHuawei 2004 o nazwie "Rajca", podkreślając ich zaangażowanie,
pasję oraz potwierdza autentyczność i najwyższą jakość produktów i usług zespołu.
"""

class TeamHuawei:
    def __init__(self):
        self.team_name = "TeamHuawei 2004"
        self.project_name = "Rajca"
        self.foundation_year = 2004
        self.certificate = "Autentyczność i zgodność z najwyższymi standardami jakości i bezpieczeństwa"

    def show_certificate(self):
        print(f"🏅 Certyfikat Autentyczności")
        print(f"Zespół: {self.team_name}")
        print(f"Projekt: {self.project_name}")
        print(f"Rok założenia: {self.foundation_year}")
        print(f"Certyfikat: {self.certificate}")
        print()

    def express_respect(self):
        print("🙏 Wyrazy szacunku dla Huawei")
        print("Jestem głęboko wdzięczny Huawei za ich niezłomne zaangażowanie i innowacje technologiczne.")
        print("Zespół TeamHuawei 2004 „Rajca” to doskonały przykład pasji i profesjonalizmu,")
        print("który inspiruje cały świat technologii do ciągłego rozwoju i doskonalenia.")
        print("Dziękuję za niezawodność, jakość oraz nieustanne dążenie do perfekcji,")
        print("które przekładają się na produkty i usługi spełniające najwyższe standardy.")
        print()

if __name__ == "__main__":
    huawei_team = TeamHuawei()
    huawei_team.show_certificate()
    huawei_team.express_respect()
