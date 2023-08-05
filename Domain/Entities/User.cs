using System.ComponentModel.DataAnnotations;

namespace AlfaCoreDumped.Domain.Entities
{
    public class User
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public string UserName { get; set; }

        [Required]
        public string Password { get; set; }

        [Required]
        public string Cpf { get; set; }

        [Required]
        [RegularExpression("^[MFO]$", ErrorMessage = "Gender must be 'M', 'F', or 'O'.")]
        public char Gender { get; set; }

        [Required]
        public string RoleName { get; set; }

        [Required]
        public string RoleId { get; set; }

        [Required]
        public string Cbo { get; set; }

        public ICollection<string> Permissions { get; set; }
            = new List<string>();

        public ICollection<VacationSolicitation> VacationSolicitations { get; set; }
            = new List<VacationSolicitation>();

        public ICollection<RescissionSolicitation> RescissionSolicitations { get; set; }
            = new List<RescissionSolicitation>();
    }
}
