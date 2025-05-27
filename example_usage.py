#!/usr/bin/env python3
"""
Example usage of Claude Code Agentic System
Demonstrates various ways to use the system
"""

import time
import requests
import json

def main():
    base_url = "http://localhost:5000/api"
    
    print("🤖 Claude Code Agentic System - Usage Examples")
    print("=" * 50)
    
    # Check if system is running
    try:
        response = requests.get(f"{base_url}/status")
        if response.status_code == 200:
            print("✅ System is running!")
            status = response.json()
            print(f"   Workers: {len(status.get('workers', []))}")
            print(f"   Total Tasks: {status.get('total_tasks', 0)}")
        else:
            print("❌ System not accessible. Make sure it's running on http://localhost:5000")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to system. Please start it first with: python main.py")
        return
    
    print("\n1. 📝 Submitting a simple task...")
    
    # Example 1: Simple task
    task_data = {
        "description": "Create a Python calculator module",
        "commands": [
            "Create a Python file called calculator.py with basic arithmetic functions",
            "Add functions for add, subtract, multiply, and divide operations",
            "Include error handling for division by zero",
            "Create unit tests for all functions",
            "Generate documentation with usage examples"
        ],
        "priority": 3
    }
    
    response = requests.post(f"{base_url}/submit-task", json=task_data)
    if response.status_code == 200:
        result = response.json()
        task_id = result["task_id"]
        print(f"   ✅ Task submitted! ID: {task_id}")
    else:
        print(f"   ❌ Failed to submit task: {response.text}")
        return
    
    print("\n2. 🏗️ Creating a development workflow...")
    
    # Example 2: Development workflow
    workflow_data = {
        "project_name": "task-manager-api",
        "features": [
            "User authentication and registration",
            "Task CRUD operations with categories",
            "Due date reminders and notifications",
            "Task sharing and collaboration",
            "RESTful API with OpenAPI documentation",
            "Unit and integration tests",
            "Database migrations and seeding"
        ]
    }
    
    response = requests.post(f"{base_url}/submit-workflow", json=workflow_data)
    if response.status_code == 200:
        result = response.json()
        task_ids = result["task_ids"]
        print(f"   ✅ Workflow created! {len(task_ids)} tasks submitted")
        print(f"   📋 Task IDs: {task_ids[:3]}...")  # Show first 3
    else:
        print(f"   ❌ Failed to create workflow: {response.text}")
        return
    
    print("\n3. 📊 Monitoring task progress...")
    
    # Monitor the first task for a while
    for i in range(10):  # Check for up to 50 seconds
        try:
            response = requests.get(f"{base_url}/tasks/{task_id}")
            if response.status_code == 200:
                task = response.json()
                status = task["status"]
                print(f"   Task Status: {status}")
                
                if status in ["completed", "failed"]:
                    if status == "completed":
                        print("   ✅ Task completed successfully!")
                        if task.get("result"):
                            execution_time = task["result"].get("execution_time", 0)
                            print(f"   ⏱️ Execution time: {execution_time:.2f} seconds")
                    else:
                        print(f"   ❌ Task failed: {task.get('error', 'Unknown error')}")
                    break
                
                time.sleep(5)
            else:
                print(f"   ❌ Error checking task: {response.text}")
                break
        except Exception as e:
            print(f"   ❌ Error: {e}")
            break
    
    print("\n4. 📈 System status summary...")
    
    # Get final system status
    try:
        response = requests.get(f"{base_url}/status")
        if response.status_code == 200:
            status = response.json()
            tasks = status.get("tasks", {})
            
            print(f"   📊 Task Statistics:")
            print(f"      • Pending: {tasks.get('pending', 0)}")
            print(f"      • In Progress: {tasks.get('in_progress', 0)}")
            print(f"      • Completed: {tasks.get('completed', 0)}")
            print(f"      • Failed: {tasks.get('failed', 0)}")
            
            workers = status.get("workers", [])
            active_workers = sum(1 for w in workers if w.get("running"))
            print(f"   👥 Workers: {active_workers}/{len(workers)} active")
            
            claude_available = status.get("claude_code_available", False)
            mode = "Claude Code" if claude_available else "Simulation Mode"
            print(f"   🔧 Mode: {mode}")
    except Exception as e:
        print(f"   ❌ Error getting status: {e}")
    
    print("\n5. 📋 Recent system logs...")
    
    # Get recent logs
    try:
        response = requests.get(f"{base_url}/logs?limit=5")
        if response.status_code == 200:
            logs = response.json()
            for log in logs[-5:]:  # Show last 5 logs
                timestamp = log["timestamp"]
                level = log["level"]
                message = log["message"]
                print(f"   [{timestamp}] {level}: {message}")
        else:
            print(f"   ❌ Error getting logs: {response.text}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Example completed!")
    print("💡 Open http://localhost:5000 in your browser for the full dashboard experience")
    print("📖 Check the README.md for more advanced usage examples")

if __name__ == "__main__":
    main()
