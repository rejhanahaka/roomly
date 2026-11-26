USE roomly;

INSERT INTO rooms (name, building, room_type, capacity) VALUES
('A1', 'Building A', 'classroom', 40),
('A3', 'Building A', 'classroom', 30),
('B12', 'Building B', 'classroom', 50),
('Lab 1', 'Building B', 'lab', 25),
('Meeting Hall', 'Main Building', 'meeting_hall', 80);

INSERT INTO timetable_entries (room_id, day_of_week, start_time, end_time, title) VALUES
(2, 1, '09:00', '11:00', 'Software Engineering'),
(4, 2, '10:00', '12:00', 'Databases Lab'),
(3, 2, '12:00', '14:00', 'Operating Systems');