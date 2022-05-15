from typing import Literal


class TreeNode:
    def __init__(self, name: str, designation: str):
        self.name = name
        self.designation = designation
        self.both = f"{self.name} ({self.designation})"
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, property_name: Literal['name', 'designation', 'both']):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + getattr(self, property_name))
        if self.children:
            for child in self.children:
                child.print_tree(property_name=property_name)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Alex", "Infrastructure Head")
    infra_head.add_child(TreeNode("Marco", "Cloud Manager"))
    infra_head.add_child(TreeNode("Claudio", "App Manager"))

    cto = TreeNode("Mark", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Steve", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Ana", "HR Head")

    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Mario", "Policy Manager"))

    ceo = TreeNode("Luca", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree(property_name="name")
    print('\n')
    root_node.print_tree(property_name="designation")
    print('\n')
    root_node.print_tree(property_name="both")