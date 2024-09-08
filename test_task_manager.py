import unittest
from unittest.mock import patch, mock_open
import task_manager

class TestTaskManager(unittest.TestCase):

    @patch("builtins.input", side_effect=["Test Task", "description", "low", "general"])
    @patch("task_manager.create_unique_id", return_value=1)
    @patch("task_manager.open", new_callable=mock_open)
    def test_add_task(self, mock_file, mock_id, mock_input):
        """Test adding a new task."""
        task_manager.add_task()
        mock_file.assert_called_with("tasks_info.csv", "a", newline='')
        mock_file().write.assert_called()  # Ensure the file is written

    @patch("task_manager.open", new_callable=mock_open, read_data="1,Test Task,description,low,general,Incomplete\n")
    def test_display_tasks(self, mock_file):
        """Test displaying tasks."""
        result = task_manager.display_tasks()
        self.assertIn("Test Task", result)  # Check if the task is displayed
        self.assertIn("Incomplete", result)

    @patch("task_manager.open", new_callable=mock_open, read_data="1,Test Task,description,low,general,Incomplete\n")
    def test_view_task_details(self, mock_file):
        """Test viewing task details."""
        with patch("builtins.input", return_value="1"):
            task_manager.view_task_prompt()
            self.assertIn("Test Task", mock_file().read())

    @patch("task_manager.open", new_callable=mock_open, read_data="1,Test Task,description,low,general,Incomplete\n")
    def test_mark_complete(self, mock_file):
        """Test marking a task as complete."""

        with patch("builtins.input", return_value="1"):
            task_manager.complete_task()
            mock_file.assert_called_with("tasks_info.csv", "w", newline='')
            written_data = mock_file().write.call_args_list
            updated_data = "".join(call[0][0] for call in written_data)
            self.assertIn("Complete", updated_data)


    @patch("task_manager.open", new_callable=mock_open, read_data="1,Test Task,description,low,general,Incomplete\n")
    def test_delete_task(self, mock_file):
        """Test deleting a task."""
        with patch("builtins.input", return_value="1"):
            task_manager.delete_task_prompt()
            self.assertIn("1,Test Task", mock_file().read())

    def test_validate_priority(self):
        """Test priority validation."""
        self.assertTrue(task_manager.validate_priority("low"))
        self.assertTrue(task_manager.validate_priority("medium"))
        self.assertTrue(task_manager.validate_priority("high"))
        self.assertFalse(task_manager.validate_priority("urgent"))

    def test_validate_non_empty(self):
        """Test non-empty validation."""
        self.assertTrue(task_manager.validate_non_empty("Title", "Task Title"))
        self.assertFalse(task_manager.validate_non_empty("", "Task Title"))

if __name__ == "__main__":
    unittest.main()
