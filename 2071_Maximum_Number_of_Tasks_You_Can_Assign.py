class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        from collections import deque
        
        # Sort tasks and workers
        tasks.sort()  # Sort tasks in ascending order (easier tasks first)
        workers.sort()  # Sort workers in ascending order (weaker workers first)
        
        def can_complete(k):
            
            if k > len(tasks) or k > len(workers):
                return False
            
            # Select k easiest tasks
            selected_tasks = tasks[:k]
            
            # Select k strongest workers
            selected_workers = workers[len(workers) - k:]
            
            # Create a queue of workers (from weakest to strongest)
            worker_queue = deque(selected_workers)
            pills_left = pills
            
            # Process tasks from hardest to easiest
            for i in range(k - 1, -1, -1):
                task = selected_tasks[i]
                
                # If the strongest worker can complete the task without a pill
                if worker_queue and worker_queue[-1] >= task:
                    worker_queue.pop()  # Use the strongest worker
                    continue
                
                # Need to use a pill
                if pills_left <= 0:
                    return False  # No pills left
                
                # Find the weakest worker who can complete the task with a pill
                idx = 0
                while idx < len(worker_queue) and worker_queue[idx] + strength < task:
                    idx += 1
                
                if idx < len(worker_queue):
                    # Found a worker who can complete the task with a pill
                    del worker_queue[idx]
                    pills_left -= 1
                else:
                    return False  # No worker can complete this task even with a pill
            
            return True
        
        # Binary search to find the maximum number of tasks
        left, right = 0, min(len(tasks), len(workers))
        
        while left < right:
            mid = (left + right + 1) // 2
            if can_complete(mid):
                left = mid
            else:
                right = mid - 1
        
        return left