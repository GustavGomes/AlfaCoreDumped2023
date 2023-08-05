using System.ComponentModel.DataAnnotations;
using AlfaCoreDumped.Domain.Entities.ExternalCandidate;
using FileObject = AlfaCoreDumped.Domain.ValueObject.FileObject;

namespace AlfaCoreDumped.Domain.Entities.ExternalReport
{
    public class Report
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public string ReporterName { get; set; }

        [Required]
        public string CostCenter { get; set; }

        [Required]
        public string Description { get; set; }

        [Required]
        public string OperationField { get; set; }

        [Required]
        public DateTime Created { get; set; }

        public string Location { get; set; }

        public ICollection<FileObject> Pictures { get; set; }
            = new List<FileObject>();
    }
}
