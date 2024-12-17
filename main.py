import icp_loop as icp


name = "Visage_symetrique_decimated.csv"

n,d = icp.ICP(name)

print(n,d)