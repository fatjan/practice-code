import copy

class SnapshotArray:
    # Constructor
    def __init__(self, length):
        self.array = [0] * length[0]
        self.snapshots = {}
        self.snapshot_id = 0

    # Function set_value sets the value at a given index idx to val. 
    def set_value(self, idx, val):
        self.array = copy.deepcopy(self.array)
        self.array[idx] = val
    
    # This function takes no parameters and returns the snapid.
    # snapid is the number of times that the snapshot() function was called minus 1. 
    def snapshot(self):
        # Replace this placeholder return statement with your code
        self.snapshots[self.snapshot_id] = self.array 
        curr_id = self.snapshot_id
        self.snapshot_id += 1
        return curr_id
    
    # Function get_value returns the value at the index idx with the given snapid.
    def get_value(self, idx, snapid):
        print(idx, snapid)
        print('self.snapshots', self.snapshots)
        if snapid not in self.snapshots:
            return -1
        # Replace this placeholder return statement with your code
        return self.snapshots[snapid][idx]

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)

input = ["SnapshotArray","set","snap","set","get","set","snap","get"] , [[3],[0,5],[],[0,6],[0,0],[0,100],[],[1,1]]

command = input[0]
args = input[1]
snapshot_obj = SnapshotArray(args[0])

for i in range(1, len(command)):
    if command[i] == "snap":
        snapshot_obj.snapshot()
    elif command[i] == "get":
        print(snapshot_obj.get_value(args[i][0], args[i][1]))
    elif command[i] == "set":
        snapshot_obj.set_value(args[i][0], args[i][1])