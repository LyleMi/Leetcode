int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize) {
  int start = costSize - 1;
  int end = 0;
  int s = gas[start] - cost[start];

  while (start > end) {
    if (s >= 0) {
      s += gas[end] - cost[end];
      end += 1;
    } else {
      start -= 1;
      s += gas[start] - cost[start];
    }
  }
  return  s >= 0 ? start : -1;
}