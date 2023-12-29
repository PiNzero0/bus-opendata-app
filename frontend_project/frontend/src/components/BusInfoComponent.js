import React from 'react';

const BusInfoComponent = ({ selectedStop, busSchedules }) => {
    return (
        <div>
            <h2>{selectedStop.name}</h2>
            <ul>
                {busSchedules.map((schedule) => (
                    <li key={schedule.id}>
                        {schedule.time} - {schedule.status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default BusInfoComponent;
