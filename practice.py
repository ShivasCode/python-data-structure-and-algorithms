class TreeNode:
    def __init__(self,data, designation):
        self.data = data
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self 
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
        
    def print_tree(self,data):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        if data == 'name':
            print(prefix + self.data)
        elif data == 'designation':
            print(prefix + self.designation)
        else:
            print(prefix + self.data + " (" + self.designation + ")")
            

        if self.children:
            for child in self.children:
                child.print_tree(data)



def build_product_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    
    infra_head = TreeNode("Vishwa", "Infrastructure head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    app_head = TreeNode("Aamir", "Application Head")

    hr_head = TreeNode("Gels", "HR Head")
    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))


    root.add_child(cto)
    root.add_child(hr_head)
    cto.add_child(infra_head)
    cto.add_child(app_head)

    return root
if __name__ == '__main__':
    root_node = build_product_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
