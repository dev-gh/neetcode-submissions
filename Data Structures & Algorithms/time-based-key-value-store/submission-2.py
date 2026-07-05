'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:

Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"

Constraints:

    1 <= key.length, value.length <= 100
    key and value only include lowercase English letters and digits.
    0 <= timestamp <= 10^7
    All the timestamps of set are strictly increasing.

'''
class TimeMap:

    def __init__(self):
        self.storage = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage.keys():
            self.storage[key] = list()

        new_val = (timestamp, value)
        self.storage[key].append(new_val)
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.storage.get(key, [])

        if len(values) == 0:
            return ""

        left = 0
        right = len(values) - 1
        last_mid = values[0]

        while left <= right:
            mid = left + (right - left) // 2

            t_timestamp, t_value = values[mid]

            print(f'{left=}, {right=}, {mid=}')

            if t_timestamp > timestamp:
                right = mid - 1
            elif t_timestamp < timestamp:
                left = mid + 1
                last_mid = values[mid]
            else:
                return t_value
            
        time , val = last_mid
        return val if time <= timestamp else ""


        
