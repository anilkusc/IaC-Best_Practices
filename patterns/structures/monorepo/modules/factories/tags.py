class Tag_Factory:
    def __init__(self,company,domain,tribe,team,squad,env,automated=True):
        self.company=company
        self.domain=domain
        self.tribe = tribe
        self.team = team
        self.squad = squad
        self.automated = automated
        self.env = env
        self.resource = self.build()
    def build(self):
        return {
            "company":self.company,
            "automated": self.automated,
            "domain": self.domain,
            "tribe": self.tribe,
            "team": self.team,
            "env": self.env,
            "squad": self.squad,
        }