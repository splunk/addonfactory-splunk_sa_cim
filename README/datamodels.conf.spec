
acceleration.allow_old_summaries = <bool>
* Optional setting. Requires 7.1+
* Sets the default value of 'allow_old_summaries' for this data model.
* Only applies to accelerated datamodels.
* When you use commands like 'datamodel', 'from', or 'tstats' to run a search 
  on this data model, allow_old_summaries=false causes the Splunk software to
  verify that the data model search in each bucket's summary metadata matches 
  the scheduled search that currently populates the data model summary.
  Summaries that fail this check are considered "out of date" and are not used 
  to deliver results for your events search.
* This setting helps with situations where the definition of an accelerated
  data model has changed, but the Splunk software has not yet updated its
  summaries to reflect this change. When allow_old_summaries=false for a data
  model, an event search of that data model only returns results from bucket
  summaries that match the current definition of the data model.
* If you set allow_old_summaries=true, your search delivers results from
  bucket summaries that are out of date with the current data model definition.
* Default: false
