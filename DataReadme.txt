README

SCHOLARS@DUKE DATA VISUALIZATION CHALLENGE DATA
   Challenge entrants need to submit an intent to submit to
   scholars-vis@duke.edu by midnight January 15, 2017. Complete details are
   available at https://rc.duke.edu/scholars-vis-challenge/

Created: November 20, 2016	by: Mark R. DeLong
Revised: 	by:

ORIGIN OF DATA
The origin of the data is the Scholars@Duke data maintained for the website
located at https:scholars.duke.edu. Julia Trimmer and Demaris Murry provided
the author and publication data; Changwei Hu used the data to derive the
author list, vocabulary list, and the co-author network matrix.

DESCRIPTION OF DATA FILES
The Scholars@Duke Data Visualization Challenge 2017 offers 5 data files and
this README file. The "scholars_publications.csv" and
"scholars_publications.xlsx" files contain identical information, provided
in two file formats; the same is the case for "scholars_faculty.csv" and 
"scholars_faculty.xlsx" files. The "coauthornet.mat" file is in Matlab 
format, and no text file format exists for this file.

If you have questions about the files, contact scholars-vis@duke.edu. 

More detailed information about the files is below.

* vocabulary.txt - a text file containing words appearing in titles and
  abstracts, 1 word per line. There are 8663 individual words, no
  duplicates, though variants of words (e.g., singular and plural forms)
  do appear.
* scholars_publications.csv (Microsoft Excel [scholars_publications.xlsx]
  format also provided) - a text file of columnar data using tab separators.
  The file has 77994 rows. Columns are:
    DUID - Duke University Unique ID (7-digit number, format: NNNNNNN)
    PRO_FIRST_NAME - author's first name
    PRO_MIDDLE_NAME - author's middle name or initial
    PRO_LAST_NAME - author's last name
    DISPLAY_NAME - author's departmental, center, or school affiliation
    TITLE - publication title
    AUTHOR_URI - Scholars@Duke web address for the author (scholars.duke.edu)
    PUBLICATION_URI - Scholars@Duke web address for the publication
      (scholars.duke.edu)
    PUBLISHED_DATE - date of the publication (format: MM/DD/YYYY 12:00 AM)
    PUBLICATION_TYPE - description of type of publication (e.g., "Scholarly
      Edition," "Report," "Other Article," "Journal Issue," "Journal Article,"
      etc.)
    ABSTRACT - abstract of the publication
    DOI - Digital Object Identifier of the publication
    ISSN - International Standard Serial Number for the publication (format:
      NNNN-NNNN)
    EISSN - Electronic International Standard Serial Number for the
      publication (format: NNNN-NNNN)
    ISBN10 - International Standard Book Number for the publication (10-digit)
    ISBN13 - International Standard Book Number for the publication (13-digit)
    JOURNAL - Title of journal
    Volume / Issue - volume number and issue number of the journal in which
      the publication appeared (format: numbers on both sides of a " / "
      separator, numbers may be nul, as in a publication without separate
      issue numbers)
* scholars_faculty.csv (Microsoft Excel [scholars_faculty.xlsx] format also
  provided) - a text file of columnar data using tab separators. The file
  has 8665 rows, showing the affiliations of faculty. Faculty may have more
  than 1 "Membership" affiliation. Columns are:
    DUID - Duke University Unique ID
    PRO_FIRST_NAME - faculty first name
    PRO_MIDDLE_NAME - faculty middle name or initial
    PRO_LAST_NAME - faculty last name
    APPOINTMENT_TYPE - "Membership," "Primary" [appointment], etc.
    TITLE - the nature of the affiliation with the organization (e.g.,
      "Member of...", "Senior Fellow of...", "Instructor of...", etc.)
    Appt Org BFR - an identifier for the organization
    Appt Org Unit - an identifier for the organization
    Appt Org Desc - the description of the organization for the affiliation
* author.txt - a text file that serves as the key to the authors included in
    coauthornet.mat. Entries are in the format:
        row index;author name;Duke University Unique ID (DUID)
    Row 1 provides the column names; data begins on row 2. Each row is for
    a single author.
* coauthornet.mat - a matrix in Matlab format showing the relationship of all
    co-authors to each other in a co-authorship network.

