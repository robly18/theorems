%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Identificacao
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{ISTPress}[2014/10/07 v0.6 ISTPress
Coleccao Ensino da Ciencia e Tecnologia]

\def\book@options{10pt,twoside}
%%% Commented because font Baskerville is not available on my environment
%%% -Duarte
\usepackage[osf]{Baskervaldx}
\def\book@font{Baskervaldx}
%\def\book@font{Baskerville}
\newif\if@miras\@mirasfalse


\DeclareOption{frame}{\@mirastrue\def\tipo@miras{frame}}
\DeclareOption{miras}{\@mirastrue\def\tipo@miras{cam}}
\DeclareOption{draft}{\edef\book@options{\book@options,draft}}

\ProcessOptions

% Baseado no estilo book.cls
\LoadClass[\book@options]{book}
\RequirePackage[portuges]{babel}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Layout
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\usepackage[papersize={169mm,235mm}, left={20mm}, right={17mm}, top={30mm}, bottom={20mm}, head={15mm}, headsep={13mm}, footskip={10mm}]{geometry}

%\usepackage[papersize={182mm,235mm},
%			left={25mm},right={25mm},top={29mm}, bottom={20mm},
%			head={15mm}, headsep={13mm},
%			footskip={10mm}
%]{geometry}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Fonte Baskerville
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Vers�o melhorada das fontes Computer Modern (para matematica)
\RequirePackage{lmodern}

\usepackage[log-declarations=false]{xparse}
\RequirePackage{fontspec}
\defaultfontfeatures{Mapping=tex-text}

%\defaultfontfeatures{Ligatures=TeX}
\setromanfont[Mapping=tex-text]{\book@font}
\setsansfont[Mapping=tex-text]{\book@font}
%\setmonofont[Mapping=tex-text]{\book@font}


% Mathfonts sizes
\DeclareMathSizes{10.5}{10}{7}{5}
\DeclareMathSizes{9}{8.5}{6}{5}
\DeclareMathSizes{8}{7.5}{6.5}{4}
\DeclareMathSizes{7}{6.6}{5}{4}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Tamanhos de letra
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\renewcommand{\baselinestretch}{1.0}
\setlength{\parindent}{0pt}
\setlength{\parskip}{7\p@ plus 4\p@ minus 2\p@}


% redefine normalsize
\renewcommand\normalsize{%
   \fontsize{10.5}{14pt}\selectfont
   \abovedisplayskip 12\p@ \@plus2\p@ \@minus5\p@
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip 8\p@ \@plus3\p@ \@minus3\p@
   \belowdisplayskip \abovedisplayskip
   \let\@listi\@listI}\normalsize 

% Header
\newcommand{\headerfont}{\fontsize{7}{10}\addfontfeatures{LetterSpace = 12}\spaceskip 4pt\selectfont}

% Section
\newcommand{\secfont}{\fontsize{10.5}{14}\spaceskip 4pt\selectfont}

% Subsection
\newcommand{\subsecfont}{\fontsize{8.5}{14}\selectfont}

% chapter
\newcommand{\chapternrfont}{\fontsize{178}{50}\fontspec[Color = FFFFFF]{\book@font}}
\newcommand{\chaptertitlefont}{\addfontfeatures{LetterSpace = 12}\spaceskip 5pt}

% Indice, prefacio e similares
\newcommand{\chaptersfont}{\fontsize{36}{30}\fontspec[Color = FFFFFF]{\book@font}}
\newcommand{\chapterscustomfont}{\fontsize{36}{30}\fontspec[Color = FFFFFF]{\book@font}}

\newcommand{\tocsectionstyle}{\fontsize{10}{10}\selectfont}
\newcommand{\tocsubsectionstyle}{\fontsize{10}{10}\selectfont}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Section, subsection e subsubsection
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\usepackage{titlesec}

\titleformat{\section}[hang]{\secfont\bfseries\uppercase}{\thesection}{1em}{}[]
\titleformat{\subsection}[hang]{\subsecfont\bfseries\uppercase}{}{0em}{}[]
\titleformat{\subsubsection}[hang]{\subsecfont\bfseries}{\thesubsection}{1em}{}[]

\titlespacing{\section}{0pt}{\parskip}{0.0pt plus 2pt minus 0pt}
\titlespacing{\subsection}{0pt}{0pt}{-7pt plus 2pt minus -2pt}
\titlespacing{\subsubsection}{0pt}{0pt}{-7pt plus 2pt minus -2pt}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% headers e footer
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{fancyhdr}

\pagestyle{fancy}\fancyhf{} 

\renewcommand{\headrulewidth}{0pt} 

\renewcommand{\chaptermark}[1]{%
	\markboth{\headerfont\MakeUppercase{#1}}%
	{\headerfont\MakeUppercase{#1}}}
\renewcommand{\sectionmark}[1]{%
	\markright{\headerfont\MakeUppercase{#1}}}

\fancyhead[RO]{\hfil\leftmark\kern0.2cm\parbox[b][7pt][b]{1 pt}%
              {\rule[0pt]{1pt}{20mm}}\rlap{\kern0.2cm\headerfont\thepage}}
\fancyhead[LE]{\strut\llap{\headerfont\thepage\kern0.2cm}\parbox[b][7pt][b]{1 pt}%
              {\rule[0pt]{1pt}{20mm}}\kern0.2cm\rightmark}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Cores
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\RequirePackage[usenames,dvipsnames]{xcolor}
\definecolor{branco}{cmyk}{0,0,0,0}
\definecolor{fundocinza}{gray}{0.80} 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Definicao de chapters
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% borrow from book.cls
\newsavebox{\thischaptername}
\newif\if@customchaptersize\@customchaptersizefalse


                    
\def\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
                       \if@mainmatter
                         \refstepcounter{chapter}%
                         \typeout{\@chapapp\space\thechapter.}%
                         \addcontentsline{toc}{chapter}%
                                   {\protect\numberline{\thechapter}\MakeUppercase{#1}}%
                       \else
                         \addcontentsline{toc}{chapter}{\protect\MakeUppercase{#1}}%
                       \fi
                    \else
                      \addcontentsline{toc}{chapter}{\MakeUppercase{#1}}%
                    \fi
                    \chaptermark{#1}%
                    \addtocontents{lof}{\protect\addvspace{10\p@}}%
                    \addtocontents{lot}{\protect\addvspace{10\p@}}%
                    \if@twocolumn
                      \@makechapterhead{#2}%
                    \else
                      \@makechapterhead{#2}%
                      \@afterheading
                    \fi}

\def\@makechapterhead#1{%
  \thispagestyle{empty}%
  \savebox{\thischaptername}{\chaptertitlefont \MakeUppercase{#1}}%
  \buildchapter
  \if@twoside \cleardoublepage \else \clearpage \fi}

\newcommand{\buildchapter}{%
	\setlength{\@tempdima}{\unitlength}
  	\setlength{\unitlength}{0.1mm}
	\begin{picture}(0,0)
	\setlength{\fboxsep}{0pt}
	\put(-280,-1810){\colorbox{fundocinza}{\makebox(1600,2170)[bl]{}}}
	\linethickness{2pt}
    \put(1220,-735){\makebox(0,0)[br]{\color{branco}\chapternrfont%
             \thechapter\kern -10pt}}
    \put(-280,-835){\color{branco} \line(1,0){1600}}
    \put(535,-935){\makebox(0,0)[tc]{\usebox{\thischaptername}}}
	\end{picture}
	\setlength{\unitlength}{\@tempdima}%
}



\def\@makeschapterhead#1{%
  \thispagestyle{empty}%
  \chaptermark{#1}%
  \if@customchaptersize  
    \buidschapter{#1}{\chapterscustomfont}
  	\@customchaptersizefalse
  \else
  	\buidschapter{#1}{\chaptersfont}
  \fi
  \vskip 40mm
  }

\def\buidschapter#1#2{%
	\setlength{\@tempdima}{\unitlength}
  	\setlength{\unitlength}{0.1mm}
	\noindent
	\begin{picture}(0,0)
	\setlength{\fboxsep}{0pt} 
	\put(-280,-360){\colorbox{fundocinza}{\makebox(1600,720)[bl]{}}} 
    \put(0,-260){\makebox(0,0)[bl]{\color{branco}#2\MakeUppercase{#1}}}
	\end{picture}
	\setlength{\unitlength}{\@tempdima}%
}
  
\newcommand{\inchapter}[2][36]{%
	\renewcommand{\chapterscustomfont}{\fontsize{#1}{30}%
	              \fontspec[Color = FFFFFF]{\book@font}}%
	\@customchaptersizetrue%
	\if@openright\cleardoublepage\else\clearpage\fi%
	\protect\@schapter{#2}\addcontentsline{toc}{chapter}{\protect\MakeUppercase{#2}}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Table of contents
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\setcounter{tocdepth}{1}

\renewcommand*\l@section{\@mytocline{1}{1.5em}{2.3em}} 
\renewcommand*\l@subsection{\@mytocline{2}{3.8em}{3.2em}}

%%%% From File: ltsect.dtx (latex.ltx)
\def\@mytocline#1#2#3#4#5{%
  \ifnum #1>\c@tocdepth 
  \else
    \vskip -\parskip  
    {%
      \leftskip #2\relax \rightskip \@tocrmarg \parfillskip -\rightskip
      \parindent #2\relax\@afterindenttrue
      \interlinepenalty\@M
      \leavevmode
      \@tempdima #3\relax
      \advance\leftskip \@tempdima \null\nobreak\hskip -\leftskip
      \ifnum #1=1 {\tocsectionstyle #4}
      \else {\tocsubsectionstyle #4}
      \fi
      \nobreak
      \hfill
      \nobreak
      \hb@xt@\@pnumwidth{\hfil\tocsectionstyle #5}%
      \par%
    }%
  \fi%
}


\renewcommand*\l@chapter[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 0.65em \@plus 6\p@ \@minus 6\p@ 
    \setlength\@tempdima{1.5em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode \bfseries
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
      \vskip 4pt plus 0pt minus 2pt 
      \penalty\@highpenalty
    \endgroup
  \fi}



\renewenvironment{thebibliography}[1]{%
  \chapter*{\bibname}
  \chaptermark{\bibname}
  \addcontentsline{toc}{chapter}{\MakeUppercase{\bibname}}
  \list{\@biblabel{\@arabic\c@enumiv}}{%
    \settowidth\labelwidth{\@biblabel{#1}}%
    \leftmargin\labelwidth
    \advance\leftmargin\labelsep
    \@openbib@code
    \usecounter{enumiv}%
    \let\p@enumiv\@empty
    \renewcommand\theenumiv{\@arabic\c@enumiv}%
  }
  \sloppy
  \clubpenalty4000
  \@clubpenalty \clubpenalty
  \widowpenalty4000%
  \sfcode`\.\@m%
}{%
  \def\@noitemerr{\@latex@warning{Empty `thebibliography' environment}}%
  \endlist%
}

\newenvironment{thechapterbibliography}[1]{%
  \section*{\MakeUppercase\bibname}
  \sectionmark{\bibname}
  \addcontentsline{toc}{section}{\numberline{}\bibname}
  \list{\@biblabel{\@arabic\c@enumiv}}{%
    \settowidth\labelwidth{\@biblabel{#1}}%
    \leftmargin\labelwidth
    \advance\leftmargin\labelsep
    \@openbib@code
    \usecounter{enumiv}%
    \let\p@enumiv\@empty
    \renewcommand\theenumiv{\@arabic\c@enumiv}%
  }%
  \sloppy
  \clubpenalty4000
  \@clubpenalty \clubpenalty
  \widowpenalty4000%
  \sfcode`\.\@m%
}{%
  \def\@noitemerr{\@latex@warning{Empty `thechapterbibliography' environment}}%
  \endlist%
}

%%%%%%%%%%%%%%%%%%%%%%
%% Indice
%%%%%

\usepackage{imakeidx}
\indexsetup{firstpagestyle=empty, noclearpage}%
%headers={\headerfont\MakeUppercase{\indexname}}{\headerfont\MakeUppercase{\indexname}}}

%\newcommand{\vchapter}[1]{%
%	\nchapter{#1}{30}
%}
%\indexsetup{level=\vchapter, firstpagestyle=empty, noclearpage,%
%headers={\headerfont\MakeUppercase{\indexname}}{\headerfont\MakeUppercase{\indexname}}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Babel customization
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand{\captionsportuges}{%
  \def\prefacename{Pref\'acio}%
  \def\refname{Refer\^encias}%
  \def\abstractname{Resumo}%
  \def\bibname{Bibliografia}%
  \def\chaptername{Cap\'{\i}tulo}%
  \def\appendixname{Ap\^endice}%
  \def\contentsname{\'Indice}%
  \def\listfigurename{Lista de Figuras}%
  \def\listtablename{Lista de Tabelas}%
  \def\indexname{\'INDICE REMISSIVO}%
  \def\figurename{Figura}%
  \def\tablename{Tabela}%
  \def\partname{Parte}%
  \def\enclname{Ap\^endice}%
  \def\ccname{C\'opia para}%
  \def\headtoname{Para}%
  \def\pagename{P\'agina}%
  \def\seename{veja}%
  \def\alsoname{veja tamb\'em}%
  \def\bioname{Bibliografia}%
  \def\agradecimentos{Agradecimentos}%
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Hifenizacao
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{xltxtra}
\declare@shorthand{portuges}{"-}{\nobreak\discretionary{-}{-}{-}\bbl@allowhyphens}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Ultimas operacoes
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\if@miras
	\usepackage[\tipo@miras,axes,a4,center]{crop} % trim marks apenas
	\newcommand*\cropfont[1]{\raisebox{14pt}{#1}}
	\crop[font=cropfont]
	% Redefinir cleardoublepage (com miras)
	\def\paginaembranco{\hbox{}\begin{picture}(0,0)\put(265,-600){\makebox(0,0)[br]%
		{{\headerfont\bfseries P\'agina \thepage\ (propositadamente em branco)}}}%
		\end{picture}\thispagestyle{empty}}
\else
	% Redefinir cleardoublepage (sem miras)
	\def\paginaembranco{\hbox{}\thispagestyle{empty}}
\fi

% Redefinir cleardoublepage
\def\cleardoublepage{\clearpage\if@twoside \ifodd\c@page\else
    \paginaembranco\newpage\if@twocolumn\hbox{}\newpage\fi\fi\fi}