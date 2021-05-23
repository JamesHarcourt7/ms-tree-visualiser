import math
from UserInterface import *
from MinimumSpanningTree import Kruskals


class Demo:

    def __init__(self):
        # Initialise pygame and display
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

        # Initialise empty graph
        self.vertices = []
        self.edges = []
        self.positions = []
        self.minimum_spanning_tree = []
        self.solved = False

        # Labels
        self.labels = []

        self.selected = -1
        self.running = True

        # Start demo
        self.run()
        pygame.quit()

    def run(self):
        # UI components
        reset_button = Button((100, 40), (80, 40), "Reset", (255, 255, 255), 20, (255, 0, 0), (220, 0, 0), self.reset)
        kruskal_button = Button((200, 40), (80, 40), "Kruskal", (255, 255, 255), 20, (0, 255, 0), (0, 220, 0), self.solve)

        # Main loop
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get position of mouse click
                    pos = pygame.Vector2(pygame.mouse.get_pos())

                    if reset_button.clicked(pos):
                        break
                    if self.solved:
                        break
                    if kruskal_button.clicked(pos):
                        break

                    # If selected is -1, another node hasn't been selected yet

                    # Check whether clicking on an existing node
                    clicked = False
                    v = -1
                    for v in range(len(self.vertices)):
                        if self.distance(pos, self.positions[v]) <= 15:
                            clicked = True
                            if self.selected == -1:
                                self.selected = v
                                print("Selected", str(v))
                            break

                    if self.selected == -1:
                        # Otherwise create node at that position
                        if not clicked:
                            self.vertices.append(len(self.vertices))
                            self.positions.append(pos)
                            self.labels.append(TextBox((pos.x, pos.y - 30), (20, 20), str(self.vertices[-1]),
                                                       (0, 0, 0), 18, (255, 255, 255)))
                    else:
                        if not clicked:
                            self.selected = -1
                        elif v != -1 and v != self.selected:
                            # Create a new edge between the selected node and the clicked node.
                            # The weight of the edge is the distance between the nodes.
                            if v < self.selected:
                                e = (v, self.selected, int(self.distance(self.positions[v], self.positions[self.selected])))
                                if e not in self.edges:
                                    self.edges.append(e)
                                    self.labels.append(
                                        TextBox(((self.positions[e[0]] + ((self.positions[e[1]]- self.positions[e[0]]) / 2)).x,
                                                 (self.positions[e[0]] + ((self.positions[e[1]]- self.positions[e[0]]) / 2)).y - 20),
                                                (20, 15), str(e[2]), (0, 0, 0), 10, (255, 255, 255)))
                                    print("Created edge", e)
                            else:
                                e = (self.selected, v, int(self.distance(self.positions[v], self.positions[self.selected])))
                                if e not in self.edges:
                                    self.edges.append(e)
                                    self.labels.append(
                                        TextBox(((self.positions[e[0]] + (
                                                    (self.positions[e[1]] - self.positions[e[0]]) / 2)).x,
                                                 (self.positions[e[0]] + ((self.positions[e[1]] - self.positions[
                                                     e[0]]) / 2)).y - 20),
                                                (20, 15), str(e[2]), (0, 0, 0), 10, (255, 255, 255)))
                                    print("Created edge", e)
                            self.selected = -1

            # Draw to screen
            self.screen.fill((255, 255, 255))

            reset_button.draw(self.screen)
            kruskal_button.draw(self.screen)

            for label in self.labels:
                label.draw(self.screen)

            for e in self.edges:
                if e in self.minimum_spanning_tree:
                    pygame.draw.line(self.screen, (0, 255, 0), (int(self.positions[e[0]].x), int(self.positions[e[0]].y)),
                                     (int(self.positions[e[1]].x), int(self.positions[e[1]].y)), 2)
                else:
                    pygame.draw.line(self.screen, (0, 0, 0), (int(self.positions[e[0]].x), int(self.positions[e[0]].y)),
                                     (int(self.positions[e[1]].x), int(self.positions[e[1]].y)), 2)
            for v in self.vertices:
                p = self.positions[v]
                if self.minimum_spanning_tree:
                    pygame.draw.circle(self.screen, (0, 255, 0), (int(p.x), int(p.y)), 15, 2)
                else:
                    if v == self.selected:
                        pygame.draw.circle(self.screen, (255, 0, 0), (int(p.x), int(p.y)), 15, 2)
                    else:
                        pygame.draw.circle(self.screen, (0, 0, 0), (int(p.x), int(p.y)), 15, 2)

            # Update display
            pygame.display.update()

        # Quit
        pygame.quit()

    @staticmethod
    def distance(v1, v2):
        s = v1 - v2
        return math.sqrt((s.x ** 2) + (s.y ** 2))

    def reset(self):
        self.vertices = []
        self.edges = []
        self.positions = []
        self.labels = []
        self.minimum_spanning_tree = []
        self.solved = False
        return True

    def solve(self):
        k = Kruskals(self.edges, self.vertices)
        self.minimum_spanning_tree = k.solve()
        self.solved = True
        return True


def text_demo():
    vertices = [n for n in range(7)]
    edges = [(0, 1, 1), (0, 3, 4), (1, 2, 2), (1, 3, 6), (1, 4, 4), (3, 4, 3), (3, 6, 4), (2, 4, 5), (2, 5, 6),
             (4, 5, 8), (5, 6, 3), (4, 6, 7)]
    Kruskals(edges, vertices)


if __name__ == "__main__":
    Demo()
