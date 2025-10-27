# UPE Game Analysis Dashboard 🎮

This project is a Streamlit-based web application that provides comprehensive analysis of gaming data and student information from UPE (Universidade de Pernambuco).

## 👥 Team Credits

- **Map Analysis:** Carlos Henrique
- **Data Analysis:** Gabriel Lopes de Albuquerque

## 🚀 Project Structure

```
├── data/
│   ├── alunos_upe.csv        # UPE students data
│   └── steam_games.json      # Steam games dataset
├── pages/
│   ├── genre_analysis.py     # Game genre analysis page
│   ├── student_map.py        # 2D student map visualization
│   ├── student_map_3d.py     # 3D student map visualization
│   └── top_rank_analysis.py  # Top games ranking analysis
├── src/
│   └── components/
│       ├── genre_analysis_section.py    # Genre analysis components
│       ├── rank_analysis_section.py     # Ranking analysis components
│       ├── student_map_3d_section.py    # 3D map visualization components
│       ├── student_map_section.py       # 2D map visualization components
│       └── utils.py                     # Utility functions
└── Home.py                   # Main application entry point
```

## 📊 Features

1. **Game Genre Analysis**
   - Pie chart visualization of game genres
   - Treemap visualization of games by genre
   - Donut chart for genre distribution
   - Interactive data exploration

2. **Student Map Visualization**
   - 2D geographical distribution of students
   - 3D map visualization for enhanced spatial analysis
   - Interactive location markers

3. **Game Ranking Analysis**
   - Top games analysis
   - Playing time statistics
   - Interactive data filtering

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/HenriqueDiass/palestra_universitaria_upe_2025.git
cd palestra_universitaria_upe_2025
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

> 💡 O comando acima instala todas as bibliotecas necessárias de uma só vez através do arquivo requirements.txt, tornando a instalação mais simples e garantindo a compatibilidade entre as versões.

## 🚀 Running the Application

To run the application:

```bash
streamlit run Home.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📱 Pages and Features

### Home Page
- Main dashboard entry point
- Overview of available analyses

### Genre Analysis
- Interactive visualization of game genres
- Multiple chart types:
  - Pie Chart: Shows distribution of gaming hours by genre
  - Treemap: Hierarchical view of games within genres
  - Donut Chart: Alternative view of genre distribution

### Student Map
- Geographic visualization of student distribution
- Available in both 2D and 3D views
- Interactive markers with student information

### Top Rank Analysis
- Analysis of top-ranked games
- Playing time statistics
- Filterable data views

## 🔧 Technical Details

The application is built using:
- **Streamlit**: For the web interface and interactive components
- **Plotly**: For interactive data visualizations
- **Pandas**: For data manipulation and analysis

## 📝 Data Sources

- `alunos_upe.csv`: Contains student information from UPE
- `steam_games.json`: Contains gaming data including genres, playtime, and rankings

## 🤝 Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Committing your changes
4. Pushing to the branch
5. Creating a Pull Request

## 📄 License

This project is licensed under the MIT License.