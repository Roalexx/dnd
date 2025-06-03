import React, { useState, useEffect } from "react";

function MultiDropdownWithDescription({
  title,
  prefix = "select",
  count = 1,
  options = [],
}) {
  const [selectedOptions, setSelectedOptions] = useState({});

  useEffect(() => {
    // reset if prefix or count changes
    setSelectedOptions({});
  }, [prefix, count]);

  return (
    <div className="class-detail-options" style={{ marginBottom: "1rem" }}>
      {title && <h4>{title}</h4>}

      {[...Array(count)].map((_, idx) => {
        const key = `${prefix}-${idx}`;
        const selectedValue = selectedOptions[key] || "";

        const filteredOptions = options.filter((opt) => {
          const optionId = opt.id?.toString();
          return (
            !Object.entries(selectedOptions).some(
              ([k, val]) => k !== key && val === optionId
            ) || selectedValue === optionId
          );
        });

        const selectedItem = options.find(
          (opt) => opt.id.toString() === selectedValue
        );

        return (
          <div key={key}>
            <select
              value={selectedValue}
              onChange={(e) =>
                setSelectedOptions((prev) => ({
                  ...prev,
                  [key]: e.target.value,
                }))
              }
              style={{
                display: "block",
                width: "100%",
                marginBottom: "0.5rem",
              }}
            >
              <option value="">Choice {idx + 1}</option>
              {filteredOptions.map((opt) => (
                <option key={opt.id} value={opt.id}>
                  {opt.name}
                </option>
              ))}
            </select>

            {selectedItem?.description && (
              <ul className="feature-list">
                <li className="feature-item">
                  <p className="feature-title">{selectedItem.name}</p>
                  <p className="feature-description">
                    {selectedItem.description}
                  </p>
                </li>
              </ul>
            )}
          </div>
        );
      })}
    </div>
  );
}

export default MultiDropdownWithDescription;
