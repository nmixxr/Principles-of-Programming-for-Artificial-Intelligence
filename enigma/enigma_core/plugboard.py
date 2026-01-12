class PlugLead:
    def __init__(self, mapping):
        if len(mapping) != 2:
            raise ValueError("PlugLead requires exactly 2 characters")
        a, b = mapping[0].upper(), mapping[1].upper()
        if a == b:
            raise ValueError(f"Cannot connect a letter to itself: {a}")
        self.a = a
        self.b = b

    def encode(self, character):
        c = character.upper()
        if c == self.a:
            return self.b
        elif c == self.b:
            return self.a
        else:
            return c


class Plugboard:
    def __init__(self, connections=None):
        self.leads = []
        self.connected_letters = set()
        if connections:
            for conn in connections:
                if isinstance(conn, str):
                    mapping = conn
                else:
                    mapping = ''.join(conn)
                self.add(PlugLead(mapping))

    def add(self, lead):
        if len(self.leads) >= 10:
            raise ValueError("Plugboard can hold maximum 10 leads")
        if lead.a in self.connected_letters or lead.b in self.connected_letters:
            raise ValueError(f"Letter already connected: {lead.a} or {lead.b}")
        self.leads.append(lead)
        self.connected_letters.add(lead.a)
        self.connected_letters.add(lead.b)

    def encode(self, c):
        result = c.upper()
        for lead in self.leads:
            result = lead.encode(result)
        return result
